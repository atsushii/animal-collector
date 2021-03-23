from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone

import datetime

from django.conf import settings


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('User must have an email address')

        user = self.model(email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, **kwargs):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = UserManager()
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email


class Animal(models.Model):
    animal_name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return '%s' % self.animal_name


class UserAnimal(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    picture_url = models.URLField(max_length=200)
    x_coordinate = models.FloatField()
    y_coordinate = models.FloatField()
    created_date = models.DateTimeField(auto_now_add=True, blank=True)
