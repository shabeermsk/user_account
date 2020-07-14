from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('email address', unique=True)
    first_name = models.CharField('first name', max_length=30, blank=True)
    last_name = models.CharField('last name', max_length=30, blank=True)
    company = models.CharField('company', max_length=100)

    date_created = models.DateTimeField('date created', auto_now_add=True)
    is_active = models.BooleanField('active', default=True)
    is_staff = models.BooleanField('is staff', default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = []
