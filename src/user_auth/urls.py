from django.urls import path

from user_auth.views import AuthRegisterView, LoginView

urlpatterns = [
    path("register", AuthRegisterView.as_view(), name="auth_register"),
    path("login", LoginView.as_view(), name="auth_login"),
]
