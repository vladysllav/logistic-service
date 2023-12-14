from rest_framework import generics

from .models import ProductItem
from .permissions import IsAdminOrReadOnly
from .serializers import ProductItemSerializer


class ListCreate(generics.ListCreateAPIView):
    queryset = ProductItem.objects.all()
    serializer_class = ProductItemSerializer
    permission_classes = (IsAdminOrReadOnly,)
