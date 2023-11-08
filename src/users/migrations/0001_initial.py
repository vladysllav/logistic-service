# Generated by Django 4.2.6 on 2023-10-25 05:08

import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "last_login",
                    models.DateTimeField(blank=True, null=True, verbose_name="last login"),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                ("email", models.EmailField(max_length=254, unique=True)),
                (
                    "password",
                    models.CharField(
                        max_length=128,
                        validators=[
                            django.core.validators.RegexValidator(
                                "^(?=.*\\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[^\\w\\s])[^\\s]{8,20}$",
                                [
                                    "password must contain 1 number (0-9)",
                                    "password must contain 1 uppercase letter",
                                    "password must contain 1 lowercase letter",
                                    "password must contain 1 non-alpha numeric",
                                    "password min 8 max 20 ch",
                                ],
                            )
                        ],
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        max_length=30,
                        validators=[
                            django.core.validators.RegexValidator(
                                "^[a-zA-Z]{2,20}$", "only letters min 2 max 20 ch"
                            )
                        ],
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        max_length=30,
                        validators=[
                            django.core.validators.RegexValidator(
                                "^[a-zA-Z]{2,20}$", "only letters min 2 max 20 ch"
                            )
                        ],
                    ),
                ),
                ("dob", models.DateField(blank=True, null=True)),
                (
                    "user_type",
                    models.CharField(
                        choices=[("client", "CLIENT"), ("admin", "ADMIN")], max_length=10
                    ),
                ),
                ("phone_number", models.CharField(blank=True, max_length=15, null=True)),
                ("is_active", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("profile_picture", models.URLField(blank=True, null=True)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all "
                        "permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
