from django.contrib.auth.models import AbstractUser
from auth_user.constants.enum import GenderInformation
from django.db import models

GENDER = [gender.value for gender in GenderInformation]
class User(AbstractUser):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10, unique=True)
    gender = models.CharField(GENDER, max_length=10)
    image_url = models.CharField(max_length=50)