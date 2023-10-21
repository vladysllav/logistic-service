from django.db import models
from django.contrib.auth.models import AbstractUser,PermissionsMixin


class CustomUser(AbstractUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    dob = models.DateField(null=True, blank=True)
    user_type = models.CharField(max_length=10, choices=[('client', 'Client'), ('admin', 'Admin')])
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    profile_picture = models.URLField(blank=True)
