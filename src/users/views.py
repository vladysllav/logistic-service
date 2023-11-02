import jwt
from django.http import JsonResponse
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from config import settings

from .models import Invitation, User, UserStatus
from .repositories import DatabaseUserRepository
from .serializers import InvitationSerializer, UserSerializer
from .services import UserService
from .utils import generate_activation_token, send_invitation_email


class UsersListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        user_service = UserService(DatabaseUserRepository())
        users = user_service.get_users_list()
        user_list = UserSerializer(users, many=True).data
        return JsonResponse(user_list, status=status.HTTP_200_OK, safe=False)


class SendInvitationView(APIView):
    """View for sending invitations to new users by administrators"""

    permission_classes = [IsAdminUser]

    def post(self, request, *args, **kwargs):
        serializer = InvitationSerializer(data=request.data)
        if serializer.is_valid():
            user_data = serializer.validated_data
            user = User.objects.create(
                email=user_data["email"],
                status=UserStatus.PENDING.value,
                last_name=user_data.get("last_name"),
                first_name=user_data.get("first_name"),
                phone_number=user_data.get("phone_number"),
                user_type=user_data.get("user_type"),
            )
            token = generate_activation_token(user)
            Invitation.objects.create(
                email=user_data["email"], inviter=request.user, token=token
            )

            # Send email
            send_invitation_email(user_data["email"], token)

            return Response(
                {"message": "Invitation sent successfully"}, status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AcceptInvitationView(APIView):
    """View for accepting user invitations and updating user details.

    This view allows users to accept invitations sent to them by administrators.
    It expects an activation token to be provided in the URL"""

    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        token = kwargs.get("token")
        try:
            decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            user = User.objects.get(
                pk=decoded_token["user_id"], status=UserStatus.PENDING.value
            )
        except (jwt.ExpiredSignatureError, jwt.InvalidTokenError, User.DoesNotExist):
            return Response(
                {"message": "Invalid token or user not found"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if user.status != UserStatus.PENDING.value:
            return Response(
                {"message": "User is not in PENDING status"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user_data = request.data
        if "first_name" in user_data:
            user.first_name = user_data["first_name"]
        if "last_name" in user_data:
            user.last_name = user_data["last_name"]
        if "phone_number" in user_data:
            user.phone_number = user_data["phone_number"]

        user.set_password(user_data["password"])
        user.status = UserStatus.ACTIVE.value
        user.save()

        Invitation.objects.filter(token=token).update(status="accepted")
        return Response(
            {"message": "Account activated successfully"}, status=status.HTTP_200_OK
        )
