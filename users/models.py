from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    username = None
    email = models.EmailField(unique=True, verbose_name="почта")
    phone = models.CharField(max_length=35, verbose_name="Номер телефона", null=True, blank=True)
    city = models.CharField(max_length=100, verbose_name="Город", default="Moscow")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
