from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from gateway.models import IdentityRecord
from gateway.serializers import IdentitySerializer


@extend_schema_view(
    list=extend_schema(
        summary="List all identity records",
        description="Retrieve a list of all identity records.",
        responses=IdentitySerializer(many=True),
    ),
    retrieve=extend_schema(
        summary="Retrieve an identity record",
        description="Retrieve a specific identity record by ID.",
        responses=IdentitySerializer,
    ),
    create=extend_schema(
        summary="Create a new identity record",
        description="Create a new identity record with the provided data.",
        request=IdentitySerializer,
        responses=IdentitySerializer,
    ),
    update=extend_schema(
        summary="Update an identity record",
        description="Update an existing identity record with the provided data.",
        request=IdentitySerializer,
        responses=IdentitySerializer,
    ),
)
class IdentityView(ModelViewSet):
    queryset = IdentityRecord.objects.all()
    serializer_class = IdentitySerializer

    def get_serializer(self, *args, **kwargs):
        serializer = self.get_serializer_class()
        if self.action in ["list", "retrieve"]:
            return serializer(context={"request_method": "GET"}, *args, **kwargs)
        if self.action == "create":
            return serializer(context={"request_method": "POST"}, *args, **kwargs)
        if self.action == "update":
            return serializer(context={"request_method": "PUT"}, *args, **kwargs)

    def finalize_response(self, request, response, *args, **kwargs):
        if isinstance(response, Response):
            response.data = {"data": response.data}
        return super().finalize_response(request, response, *args, **kwargs)
