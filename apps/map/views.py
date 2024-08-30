# apps/map/views.py
from rest_framework import viewsets
from .models import Marker
from .serializers import MarkerSerializer
from django.views.generic import TemplateView


class MarkerViewSet(viewsets.ModelViewSet):
    queryset = Marker.objects.all()
    serializer_class = MarkerSerializer

class MapView(TemplateView):
    template_name = 'map/map.html'
