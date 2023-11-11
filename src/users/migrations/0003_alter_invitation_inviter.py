import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_alter_user_options_alter_user_managers_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="invitation",
            name="inviter",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="user_type",
            field=models.CharField(
                choices=[("Client", "CLIENT"), ("Admin", "ADMIN"), ("Employee", "EMPLOYEE")],
                default="Client",
                max_length=10,
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="is_google_auth",
            field=models.BooleanField(default=False),
        ),
    ]
