from django.urls import path

from . import views

app_name = 'additions'

urlpatterns = [
    path('', views.index, name='index'),
]