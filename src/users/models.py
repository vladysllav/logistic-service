from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from enum import Enum, unique


@unique
class UserType(Enum):
    CLIENT = 'client'
    ADMIN = 'admin'


class User(AbstractUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    dob = models.DateField(null=True, blank=True)
    user_type = models.CharField(max_length=10, choices=[(tag.value, tag.name) for tag in UserType])
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    profile_picture = models.URLField(blank=True, null=True)
