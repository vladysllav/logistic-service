from django.contrib import admin

from .models import Product, ProductItem

admin.site.register(ProductItem)
admin.site.register(Product)
