import random
import string
from .managers import CustomUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser


class SoftwareLicenseKey(models.Model):
    def license_generate():
        return ''.join(
            random.choices(string.ascii_uppercase + string.digits, k=30))
    name = models.CharField(max_length=50)
    key = models.CharField(max_length=30, default=license_generate)
    is_used = models.BooleanField(default=False)

    def __str__(self):
        return self.key


class User(AbstractUser):
    username = None
    email = models.EmailField('Email address', unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    software_license_key = models.ForeignKey(
        SoftwareLicenseKey, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.email
