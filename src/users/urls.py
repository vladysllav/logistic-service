from django.urls import path

from .views import AcceptInvitationView, SendInvitationView, UsersListView

urlpatterns = [
    path("users/", UsersListView.as_view(), name="users-list"),
    path("send-invitation/", SendInvitationView.as_view(), name="send-invitation"),
    path(
        "accept-invitation/<str:token>/",
        AcceptInvitationView.as_view(),
        name="accept-invitation",
    ),
]
