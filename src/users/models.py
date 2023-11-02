from enum import Enum, unique

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core import validators as val
from django.db import models

from users.managers import UserManager
from users.utils import RegEx


@unique
class UserType(Enum):
    CLIENT = "Client"
    ADMIN = "Admin"
    EMPLOYEE = "Employee"


@unique
class UserStatus(Enum):
    ACTIVE = "Active"
    INACTIVE = "Inactive"
    PENDING = "Pending"


class User(AbstractBaseUser, PermissionsMixin):
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
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    profile_picture = models.URLField(blank=True, null=True)
    status = models.CharField(
        max_length=10,
        choices=[(tag.value, tag.name) for tag in UserStatus],
        default=UserStatus.ACTIVE.value,
    )
    # username = None

    USERNAME_FIELD = "email"

    objects = UserManager()


class Invitation(models.Model):
    email = models.EmailField()
    inviter = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=10,
        choices=[(tag.value, tag.name) for tag in UserStatus],
        default=UserStatus.PENDING.value,
    )
    token = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
