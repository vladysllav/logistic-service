from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            user_type = request.user.user_type
        else:
            user_type = False
        is_true = user_type == "admin"
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(is_true)
