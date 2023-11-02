from django.contrib.gis.db import models


class Warehouse(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.CharField(max_length=255)
    location = models.PointField()
    area_size = models.IntegerField()
