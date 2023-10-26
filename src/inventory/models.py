from django.db import models

from users.models import User


class Warehouse(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)


class Product(models.Model):
    name = models.CharField(max_length=255)
    warehouse = models.ForeignKey(
        Warehouse, related_name="products", on_delete=models.CASCADE
    )
    quantity_in_stock = models.PositiveIntegerField()


class Transport(models.Model):
    warehouse_from = models.ForeignKey(
        Warehouse, related_name="cars_from", on_delete=models.CASCADE
    )
    warehouse_to = models.ForeignKey(
        Warehouse, related_name="cars_to", on_delete=models.CASCADE
    )
    products = models.ManyToManyField(Product)


class EmployeeWarehouseRelation(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
