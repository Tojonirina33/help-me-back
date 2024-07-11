from random import choice
from string import ascii_uppercase, digits

from django.contrib.auth.models import AbstractUser
from django.db import models

USER_TYPE_CHOICES = (
    ("regular_user", "Regular User"),
    ("medical_staff", "Medical Staff"),
    ("civil_registrar", "Civil Registrar"),
)

IDENTITY_STATUS_CHOICES = (
    ("pending", "pending"),
    ("rejected", "rejected"),
    ("done", "done"),
)

SEXE_CHOICES = (("male", "male"), ("female", "female"))


class IdentityRecord(models.Model):
    identity_key = models.CharField(max_length=20)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    sexe = models.CharField(max_length=10, choices=SEXE_CHOICES)
    birth_date = models.DateField(auto_now=False, auto_now_add=False)
    birth_place = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    profession = models.CharField(max_length=100, default="")
    distinctive_trait = models.CharField(max_length=100, blank=True)
    status = models.CharField(
        max_length=20, choices=IDENTITY_STATUS_CHOICES, default="pending"
    )
    father = models.ForeignKey(
        "IdentityRecord",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="+",
    )
    mother = models.ForeignKey(
        "IdentityRecord",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="+",
    )

    @staticmethod
    def generate_identity_id(length=12):
        chars = ascii_uppercase + digits
        id = "".join(choice(chars) for _ in range(length))
        return id


class User(AbstractUser):
    first_name = None
    last_name = None
    user_type = models.CharField(
        max_length=30, choices=USER_TYPE_CHOICES, default="regular_user"
    )
    identity = models.OneToOneField(to=IdentityRecord, on_delete=models.CASCADE)
