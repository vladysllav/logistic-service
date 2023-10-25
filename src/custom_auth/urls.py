from django.urls import path

from custom_auth.views import AuthRegisterView, TokenPairView

urlpatterns=[
    path("register",  AuthRegisterView.as_view(), name='auth_register' ),
    path('login', TokenPairView.as_view(), name='auth_login'),

]

