from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from users.serializers import UserSerializer

from .serializers import TokenSerializer, UserSignUpSerializer


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

        user_data = UserSerializer(user).data

        return Response(
            {"access_token": access_token, "refresh_token": refresh_token, "user": user_data},
            status=status.HTTP_201_CREATED,
        )


class LoginView(TokenObtainPairView):
    """
    User login
    """

    serializer_class = TokenSerializer
