from django.urls import path
from .views import home_page, category_movie, detail_category, detail_movie, create_movie, delete_movie, update_movie

urlpatterns = [
    path('', home_page, name='homepage'),
    path('category-movie', category_movie, name='category-movie'),
    path('add', create_movie, name='add'),
    path('detail-category/<int:pk>', detail_category, name='detail-category'),
    path('detail-movie/<int:pk>', detail_movie, name='detail-movie'),
    path('delete-movie/<int:pk>', delete_movie, name='delete-movie'),
    path('update-movie/<int:pk>', update_movie, name='update-movie'),
]


