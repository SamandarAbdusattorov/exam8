from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import BooleanField


class User(AbstractUser):
    is_deleted = BooleanField(default=False)

    def __str__(self):
        return self.username
