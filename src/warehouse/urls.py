from django.urls import path

from .views import WarehouseAPIDetailView, WarehouseAPIList, WarehouseAPIUpdate

urlpatterns = [
    path("list", WarehouseAPIList.as_view(), name="list"),
    path("list/<int:pk>/", WarehouseAPIUpdate.as_view()),
    path("detail/<int:pk>/", WarehouseAPIDetailView.as_view()),
]
