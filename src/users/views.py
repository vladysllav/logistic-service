import jwt
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from config import settings

from .models import Invitation, InvitationStatus, User
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

            user = User.objects.create(status=InvitationStatus.PENDING.value, **user_data)

            invitation = Invitation.objects.create(
                email=user_data["email"], inviter=request.user, user=user
            )
            token = generate_activation_token(invitation.id)
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

            invitation_id = decoded_token["invitation_id"]
            invitation = Invitation.objects.get(pk=invitation_id)

        except (jwt.ExpiredSignatureError, jwt.InvalidTokenError, Invitation.DoesNotExist):
            return Response(
                {"message": "Invalid token or invitation not found"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user_data = request.data
        user = invitation.user

        serializer = UserSerializer(user, data=user_data, partial=True)
        if serializer.is_valid():
            user = serializer.save()
            user.password = make_password(user_data["password"])
            user.status = InvitationStatus.ACTIVE
            user.save()

            invitation.status = InvitationStatus.ACTIVE
            invitation.save()

            return Response(
                {"message": "Account activated successfully"}, status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
