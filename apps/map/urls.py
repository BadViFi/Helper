# apps/map/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MarkerViewSet, MapView

router = DefaultRouter()
router.register(r'markers', MarkerViewSet, basename='marker')

app_name = 'map'
urlpatterns = [
    path('', MapView.as_view(), name='map_view'),
    path('api/', include(router.urls)),
]
