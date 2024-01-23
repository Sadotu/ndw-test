# models/bridge_record.py

from django.db import models
from .bridge_administration import BridgeAdministration


class BridgeRecord(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    administration = models.ForeignKey(BridgeAdministration, on_delete=models.CASCADE, related_name='records')
    announced = models.DateTimeField()
    open = models.DateTimeField(null=True, blank=True)  # `blank=True` is added to allow field to be blank in forms.
    closed = models.DateTimeField(null=True, blank=True)  # Same as above for consistency in form handling.
    special = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Record {self.id}"
