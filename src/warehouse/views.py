from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from .models import Warehouse
from .permissions import IsAdminOrReadOnly
from .serializers import WarehouseSerializer


class WarehouseAPIList(generics.ListCreateAPIView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
    permission_classes = (IsAdminOrReadOnly,)


class WarehouseAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
    permission_classes = (IsAdminOrReadOnly,)


class WarehouseAPIDestroyView(generics.RetrieveDestroyAPIView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
    permission_classes = (IsAdminUser,)
