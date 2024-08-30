from django.db import models
from django.contrib.auth.models import User

from django.urls import reverse

class Marker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Користувач', related_name='map')
    description = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f"{self.description} ({self.latitude}, {self.longitude})"

    def get_absolute_url(self):
        return reverse('map:description', args=[self.id])

    class Meta:
        verbose_name = 'Маркер'
        verbose_name_plural = 'Маркери'
        db_table = 'map_marker'

