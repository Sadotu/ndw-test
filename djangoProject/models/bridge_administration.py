# models/bridge_administration.py

from django.db import models
from django.contrib.gis.db import models as gis_models


class BridgeAdministration(models.Model):
    name = models.CharField(max_length=255)
    location = gis_models.GeometryField()  # Use PointField, PolygonField, etc., as appropriate for the type of geometry
    ris_index = models.CharField(max_length=255)
    vild_location = models.BigIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Bridge Administrations"
