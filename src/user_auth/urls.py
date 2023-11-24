from django.urls import path

from user_auth.views import AuthRegisterView, GoogleAuthView, LoginView

urlpatterns = [
    path("register", AuthRegisterView.as_view(), name="auth_register"),
    path("login", LoginView.as_view(), name="auth_login"),
    path("google-auth", GoogleAuthView.as_view(), name="google-auth"), 
]
