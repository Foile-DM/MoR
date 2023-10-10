from django.contrib import admin
from .models import Material, Product, ProductMaterial

# Register your models here.

admin.site.register(Material)
admin.site.register(Product)
admin.site.register(ProductMaterial)
