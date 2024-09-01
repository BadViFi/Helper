from django.urls import path
from . import views

app_name = 'additions'

urlpatterns = [
    path('', views.AdditionsListView.as_view(), name='list_additions'),
    path('addition/create/', views.PostCreateView.as_view(), name='create'),
    path('<int:id>/', views.AdditionDetailView.as_view(), name='detale'),
    path('add-favorite/<int:addition_id>/', views.AddFavoriteView.as_view(), name='add_favorite'),
    path('<int:detale_id>/comment/', views.comment, name='comment'),
    path('<int:detale_id>/comment/<int:comment_id>/like/', views.like_comment, name='like_comment'),
    path('<int:id>/edit_addition/', views.UpdateAdditionView.as_view(), name="edit_addition"),
    path('<int:id>/delete_addition/',views.AdditionDeleteView.as_view(),name="delete_addition")
]

