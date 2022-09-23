from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=256)
    email = models.EmailField(max_length=256, unique=True)
    password = models.CharField(max_length=256)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

