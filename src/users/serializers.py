from rest_framework import serializers

from .models import Invitation, User, UserType


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
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


class InvitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invitation
        fields = [
            "email",
            "last_name",
            "user_type",
            "phone_number",
            "first_name",
            "user_type",
        ]

    last_name = serializers.CharField(
        required=False,
        allow_blank=True,
    )
    first_name = serializers.CharField(required=False, allow_blank=True)
    user_type = serializers.ChoiceField(
        choices=[(tag.value, tag.name) for tag in UserType], required=False, allow_blank=True
    )
    phone_number = serializers.CharField(required=False, allow_blank=True)
