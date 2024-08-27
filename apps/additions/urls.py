from django.urls import path
from . import views

app_name = 'additions'

urlpatterns = [

    path('', views.AdditionsListView.as_view(), name='list_additions'),
    path('post/create/', views.PostCreateView.as_view(), name='create'),

    path('<int:detale_id>/', views.get_detale, name='detale'),
    

    path('<int:detale_id>/comment/', views.comment, name='comment'),
    path('<int:detale_id>/comment/<int:comment_id>/like/', views.like_comment, name='like_comment')
]

