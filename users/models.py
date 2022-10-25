from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    username = models.CharField(max_length=200, null=False, unique=True, verbose_name='Логин')
    first_name = models.CharField(max_length=200, verbose_name='Имя пользователя', blank=True)
    last_name = models.CharField(max_length=200, verbose_name='Фамилия пользователя', blank=True)
    email = models.EmailField(verbose_name='Имейл', blank=True)
    password = models.TextField(null=False, verbose_name='Пароль')

    def __str__(self):
        return self.username
