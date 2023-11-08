from django.urls import path

from .views import ListCreate, RetrieveDestroy, RetrieveUpdate

urlpatterns = [
    path("", ListCreate.as_view(), name="list"),
    path("<int:pk>/", RetrieveUpdate.as_view()),
    path("delete/<int:pk>/", RetrieveDestroy.as_view()),
]
