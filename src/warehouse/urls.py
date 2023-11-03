from django.urls import path

from .views import WarehouseAPIDestroyView, WarehouseAPIList, WarehouseAPIUpdate

urlpatterns = [
    path("", WarehouseAPIList.as_view(), name="list"),
    path("<int:pk>/", WarehouseAPIUpdate.as_view()),
    path("delete/<int:pk>/", WarehouseAPIDestroyView.as_view()),
]
