from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_client_user = models.BooleanField(default=False, verbose_name="É cliente")
