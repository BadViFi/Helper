from django.urls import path
from . import views

app_name = 'additions'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:detale_id>/', views.get_detale, name='detale'),
    path('create/', views.create, name='create'),
    path('<int:detale_id>/comment/', views.comment, name='comment'),
]
