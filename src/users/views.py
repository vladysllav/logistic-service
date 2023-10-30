from django.http import JsonResponse
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from .repositories import DatabaseUserRepository
from .services import UserService


class UsersListView(APIView):
    permission_classes = [AllowAny]

    def get(self, requests):
        user_service = UserService(DatabaseUserRepository())
        users = user_service.get_users_list()
        user_list = [
            {
                "user_id": user.id,
                "user_type": user.user_type,
                "email": user.email,
                "fist_name": user.first_name,
                "last_name": user.last_name,
            }
            for user in users
        ]

        return JsonResponse(user_list, status=status.HTTP_200_OK, safe=False)
