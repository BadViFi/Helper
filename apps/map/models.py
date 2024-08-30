from django.db import models
from django.contrib.auth.models import User

class Marker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Користувач', related_name='map')
    description = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Маркер'
        verbose_name_plural = 'Маркери'
        db_table = 'map_marker'
