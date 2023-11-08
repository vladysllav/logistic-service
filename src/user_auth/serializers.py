from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users.models import User, UserType
from users.serializers import UserSerializer


class UserSignUpSerializer(serializers.ModelSerializer):
    """Serializer for user registration"""

    class Meta:
        model = User
        fields = ("email", "password", "first_name", "last_name")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        validated_data["user_type"] = UserType.CLIENT.value
        user = super().create(validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user


class TokenSerializer(TokenObtainPairSerializer):
    """
    Serializer for obtaining and validating user tokens.
    """

    def validate(self, attrs):
        data = super().validate(attrs)
        data["user"] = UserSerializer(self.user).data
        return data


class GoogleAuth(serializers.Serializer):
    """Serializer for google"""

    email = serializers.EmailField()
    token = serializers.CharField()
