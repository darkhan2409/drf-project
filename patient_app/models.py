from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import PatientManager


class Patient(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(max_length=25, unique=True)
    birth_date = models.DateField(auto_now=False, blank=True, null=True)
    region = models.CharField(max_length=20, blank=True, null=True)
    phone = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=50, unique=True, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = PatientManager()

    def __str__(self) -> str:
        return str(self.username)




