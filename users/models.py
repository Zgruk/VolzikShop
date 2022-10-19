from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    username = models.CharField(max_length=200, null=False, unique=True, verbose_name='Имя пользователя')
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.TextField(null=False)

    def __str__(self):
        return self.username
