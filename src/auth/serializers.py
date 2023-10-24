from django.db import transaction
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from src.users.models import User, UserType


class UserSerializer(serializers.ModelSerializer):
    """ Serializer for user registration """

    class Meta:
        model = User
        fields = ("email", "password", "first_name", "last_name")
        extra_kwargs = {'password': {'write_only': True}}

    @transaction.atomic
    def create(self, validated_data: dict):
        validated_data['user_type'] = UserType.CLIENT.value
        user = User.objects.create_user(**validated_data)
        return user


class TokenPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        data['user'] = UserSerializer(self.user).data
        return data
