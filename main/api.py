from rest_framework import viewsets, permissions
from .models import Material, Product, ProductMaterial
from .serializers import MaterialSerializer, ProductSerializer, ProductMaterialSerializer


class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = MaterialSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ProductSerializer


class ProductMaterialViewSet(viewsets.ModelViewSet):
    queryset = ProductMaterial.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ProductMaterialSerializer
