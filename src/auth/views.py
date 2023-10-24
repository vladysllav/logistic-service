from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from src.auth.serializers import UserSerializer, TokenPairSerializer
from rest_framework.generics import CreateAPIView


class AuthRegisterView(CreateAPIView):
    """
    Register user
    """
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class TokenPairView(TokenObtainPairView):
    """
        User login
    """
    serializer_class = TokenPairSerializer
