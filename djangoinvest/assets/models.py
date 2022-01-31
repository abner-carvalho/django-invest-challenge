from django.conf import settings
from django.db import models
from django.utils import timezone


class Asset(models.Model):
    long_name  = models.CharField(max_length=200)
    symbol     = models.CharField(max_length=50)
    thumbnail  = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)

    # Metadados
    class Meta:
        ordering = ['-symbol']

    def publish(self):
        self.updated_at = timezone.now()
        self.save()

    def __str__(self):
        return self.symbol