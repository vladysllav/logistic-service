from django.db import models

from config.timesumped import TimesumpedModel
from warehouse.models import Warehouse


class Product(TimesumpedModel, models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    photo = models.CharField()
    sku = models.CharField(max_length=255)
    warehouses = models.ManyToManyField(Warehouse, through="ProductItem", blank=True)


class ProductItem(TimesumpedModel, models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Product")
    stock_qty = models.IntegerField(verbose_name="")
    warehouse = models.ForeignKey(
        Warehouse, on_delete=models.CASCADE, verbose_name="Warehouse", blank=True, null=True
    )
