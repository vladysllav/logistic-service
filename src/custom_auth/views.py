from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from custom_auth.serializers import UserSerializer, UserSignUpSerializer
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken


class AuthRegisterView(CreateAPIView):
    """
    Register user and issue tokens
    """
    serializer_class = UserSignUpSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)

        user_data = {
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
        }

        return Response({
            "user": user_data,
            "access_token": access_token,
            "refresh_token": refresh_token
        }, status=status.HTTP_201_CREATED)


class TokenPairView(TokenObtainPairView):
    """
        User login
    """
    serializer_class = UserSerializer

