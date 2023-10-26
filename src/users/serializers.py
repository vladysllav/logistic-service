from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "email",
            "password",
            "first_name",
            "last_name",
            "dob",
            "user_type",
            "phone_number",
            "is_active",
            "created_at",
            "updated_at",
            "profile_picture",
        )
        extra_kwargs = {"password": {"write_only": True}}
