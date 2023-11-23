from enum import Enum, unique

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core import validators as val
from django.db import models
from django.utils.translation import gettext as _

from .managers import UserManager
from .utils import RegEx


class TimesumpedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


@unique
class UserType(Enum):
    CLIENT = "Client"
    ADMIN = "Admin"
    EMPLOYEE = "Employee"


class InvitationStatus(models.TextChoices):
    ACTIVE = "Active", _("Active")
    INACTIVE = "Inactive", _("Inactive")
    PENDING = "Pending", _("Pending")


class User(TimesumpedModel, AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_google_auth = models.BooleanField(default=False)
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
        max_length=10,
        choices=[(tag.value, tag.name) for tag in UserType],
        default=UserType.CLIENT.value,
    )
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    profile_picture = models.URLField(blank=True, null=True)
    status = models.CharField(
        max_length=10,
        choices=InvitationStatus.choices,
        default=InvitationStatus.ACTIVE,
    )

    USERNAME_FIELD = "email"

    objects = UserManager()


class Invitation(TimesumpedModel, models.Model):
    email = models.EmailField()
    inviter = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=10,
        choices=InvitationStatus.choices,
        default=InvitationStatus.PENDING,
    )
