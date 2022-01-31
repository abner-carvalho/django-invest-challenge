from django.conf import settings
from django.db import models
from django.utils import timezone


class Asset(models.Model):
    long_name  = models.CharField(max_length=200)
    symbol     = models.CharField(max_length=50, unique=True)
    thumbnail  = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Metadados
    class Meta:
        ordering = ['-symbol']

    def __str__(self):
        return self.symbol