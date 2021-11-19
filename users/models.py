from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager

class CustomUserManagoer(UserManager):
    def _create_user(self, email, password, **extra_field):
        if not email:
            raise ValueError("input email")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_field)
        user.password = make_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, **extra_fields)
        

class User(AbstractBaseUser):
    email = models.CharField(max_length=30, unique=True)
    name  = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    objects = CustomUserManagoer()