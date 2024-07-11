from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.core.exceptions import ValidationError as DjangoValidationError
from django.db.utils import IntegrityError
from rest_framework import serializers

from gateway.models import IdentityRecord


class IdentitySerializer(serializers.ModelSerializer):

    class Meta:
        model = IdentityRecord
        fields = "__all__"

    def get_fields(self):
        fields = super().get_fields()
        request_method = self.context.get("request_method")
        if request_method == "GET":
            self.Meta.depth = 1
        if request_method == "POST":
            self.Meta.read_only_fields = ["identity_key"]
        if request_method == "PUT":
            self.Meta.read_only_fields = [
                "identity_key",
                "birth_date",
                "birth_place",
                "sexe",
            ]
            for field_name, field in fields.items():
                if field_name in ["first_name", "address"]:
                    field.required = False
        return fields

    def __parent_validation(self, value, parent_key):
        sexe = "male" if parent_key == "father" else "female"
        if value.sexe != sexe:
            raise serializers.ValidationError(
                {parent_key: f"{parent_key} sexe must be a {sexe}"}
            )
        return value

    def validate_father(self, value):
        return self.__parent_validation(value, "father")

    def validate_mother(self, value):
        return self.__parent_validation(value, "mother")

    def create(self, validated_data):
        validated_data["identity_key"] = IdentityRecord.generate_identity_id()
        return super().create(validated_data)


class CustomUserDetailsSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField()
    user_type = serializers.CharField()
    identity = IdentitySerializer()


class JWTSerializer(serializers.Serializer):

    access = serializers.CharField()
    refresh = serializers.CharField()
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        user_data = CustomUserDetailsSerializer(obj["user"], context=self.context).data
        return user_data


class CustomRegisterSerializer(RegisterSerializer):
    email = None
    identity_key = serializers.CharField(allow_blank=False)

    def validate(self, data):
        super().validate(data)
        if "identity_key" in data:
            try:
                identity_record = IdentityRecord.objects.get(
                    identity_key=data["identity_key"]
                )
            except IdentityRecord.DoesNotExist:
                raise serializers.ValidationError(
                    {"identity_key": "This identity key does not exist"}
                )
            data["identity"] = identity_record
        return data

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        user.identity = self.validated_data["identity"]
        self.cleaned_data = self.get_cleaned_data()
        user = adapter.save_user(request, user, self, commit=False)
        if "password1" in self.cleaned_data:
            try:
                adapter.clean_password(self.cleaned_data["password1"], user=user)
            except DjangoValidationError as exc:
                raise serializers.ValidationError(
                    detail=serializers.as_serializer_error(exc)
                )
        try:
            user.save()
        except IntegrityError as exc:
            raise serializers.ValidationError(
                {"identity_key": ["This identity key is already used"]}
            )
        self.custom_signup(request, user)
        setup_user_email(request, user, [])
        return user
