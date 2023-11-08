from rest_framework import generics

from .models import Warehouse
from .permissions import IsAdminOrReadOnly
from .serializers import WarehouseSerializer


class ListCreate(generics.ListCreateAPIView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
    permission_classes = (IsAdminOrReadOnly,)


class RetrieveUpdate(generics.RetrieveUpdateAPIView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
    permission_classes = (IsAdminOrReadOnly,)


class RetrieveDestroy(generics.RetrieveDestroyAPIView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
    permission_classes = (IsAdminOrReadOnly,)
