from django.urls import path

from src.auth.views import AuthRegisterView, TokenPairView

urlpatterns = [
    path("api/v1/register", AuthRegisterView.as_view(), name='auth_register'),
    path('api/v1/login', TokenPairView.as_view(), name='auth_login'),

]
