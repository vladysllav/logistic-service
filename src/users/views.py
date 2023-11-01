from django.http import JsonResponse
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from .repositories import DatabaseUserRepository
from .serializers import UserSerializer
from .services import UserService


class UsersListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        user_service = UserService(DatabaseUserRepository())
        users = user_service.get_users_list()
        user_list = UserSerializer(users, many=True).data
        return JsonResponse(user_list, status=status.HTTP_200_OK, safe=False)
