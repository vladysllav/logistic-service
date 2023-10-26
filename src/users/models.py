from enum import Enum, unique

from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.core import validators as val
from django.db import models

from users.managers import UserManager
from users.utils import RegEx


@unique
class UserType(Enum):
    CLIENT = "client"
    ADMIN = "admin"
    EMPLOYEE = "employee"


class User(AbstractUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    password = models.CharField(
        max_length=128,
        validators=[val.RegexValidator(RegEx.PASSWORD.pattern, RegEx.PASSWORD.msg)],
    )
    first_name = models.CharField(
        max_length=30, validators=[val.RegexValidator(RegEx.NAME.pattern, RegEx.NAME.msg)]
    )
    last_name = models.CharField(
        max_length=30, validators=[val.RegexValidator(RegEx.NAME.pattern, RegEx.NAME.msg)]
    )
    dob = models.DateField(null=True, blank=True)
    user_type = models.CharField(
        max_length=10, choices=[(tag.value, tag.name) for tag in UserType]
    )
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    profile_picture = models.URLField(blank=True, null=True)
    username = None

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = []

    objects = UserManager()
