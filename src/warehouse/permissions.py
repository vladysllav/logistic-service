from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        if request.user.user_type == "admin":
            return True
        if request.method in permissions.SAFE_METHODS:
            return True
