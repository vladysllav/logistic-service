# Generated by Django 4.2.6 on 2023-10-26 15:26

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="user",
            managers=[],
        ),
        migrations.RemoveField(
            model_name="user",
            name="username",
        ),
    ]
