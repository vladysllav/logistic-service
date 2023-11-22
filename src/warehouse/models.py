from django.contrib.gis.db.models import PointField
from django.db import models


class Warehouse(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.CharField(max_length=255)
    location = PointField()
    area_size = models.IntegerField()
    products = models.ManyToManyField(
        "products.Product",
        through="products.ProductItem",
        verbose_name="Products",
        blank=True,
    )
