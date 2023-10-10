from rest_framework import routers
from .api import MaterialViewSet, ProductViewSet, ProductMaterialViewSet


routers = routers.DefaultRouter()
routers.register('api/material', MaterialViewSet, 'material')
routers.register('api/product', ProductViewSet, 'product')
routers.register('api/product-material', ProductMaterialViewSet, 'product-material')


urlpatterns = routers.urls
