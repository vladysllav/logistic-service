from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from enum import Enum, unique
from utils import RegEx
from django.core import validators as val


@unique
class UserType(Enum):
    CLIENT = 'client'
    ADMIN = 'admin'


class User(AbstractUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128, validators=[
        val.RegexValidator(RegEx.PASSWORD.pattern, RegEx.PASSWORD.msg)
    ])
    first_name = models.CharField(max_length=30,validators=[val.RegexValidator(RegEx.NAME.pattern, RegEx.NAME.msg)])
    last_name = models.CharField(max_length=30,validators=[val.RegexValidator(RegEx.NAME.pattern, RegEx.NAME.msg)])
    dob = models.DateField(null=True, blank=True)
    user_type = models.CharField(max_length=10, choices=[(tag.value, tag.name) for tag in UserType])
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    profile_picture = models.URLField(blank=True, null=True)
