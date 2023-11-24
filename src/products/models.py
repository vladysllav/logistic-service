from django.db import models

from warehouse.models import Warehouse


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    photo = models.CharField()
    sku = models.CharField(max_length=255)
    created_at = models.DateTimeField(verbose_name="Created", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Last update", auto_now_add=True)
    warehouse = models.ManyToManyField(Warehouse, through="ProductItem", blank=True)


class ProductItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Product")
    stock_qty = models.IntegerField(verbose_name="")
    warehouse = models.ForeignKey(
        Warehouse, on_delete=models.CASCADE, verbose_name="Warehouse", blank=True, null=True
    )
