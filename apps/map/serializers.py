# apps/map/serializers.py
from rest_framework import serializers
from .models import Marker


class MarkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marker
        fields = ['id', 'user', 'description', 'latitude', 'longitude']
