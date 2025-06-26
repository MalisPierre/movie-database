from django.urls import path
from movie.views_genre import ApiOverview as GenreOverview, add_movie_genre, read_movie_genre, read_detail_movie_genre, update_movie_genre, delete_movie_genre
from movie.views_movie import ApiOverview as MovieOverview, add_movie, read_movie, read_detail_movie, update_movie, delete_movie

urlpatterns = [
    path('movie/', MovieOverview, name='movie_home'),
    path('movie/create/', add_movie, name='add_movie'),
    path('movie/list/', read_movie.as_view(), name='read_movie'),
    path('movie/read/<int:pk>/', read_detail_movie.as_view(), name='read_movie'),
    path('movie/update/<int:pk>/', update_movie, name='update_movie'),
    path('movie/item/<int:pk>/delete/', delete_movie, name='delete_movie'),

    path('genre/', GenreOverview, name='movie_home'),
    path('genre/create/', add_movie_genre, name='add_movie_genre'),
    path('genre/list/', read_movie_genre, name='read_movie_genre'),
    path('genre/read/<int:pk>/', read_detail_movie_genre.as_view(), name='read_movie_genre'),
    path('genre/update/<int:pk>/', update_movie_genre, name='update_movie_genre'),
    path('genre/item/<int:pk>/delete/', delete_movie_genre, name='delete_movie_genre'),
]