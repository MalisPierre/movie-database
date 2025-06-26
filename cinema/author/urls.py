from django.urls import path
from author.views_author import ApiOverview as AuthorReview, add_author, read_author, read_detail_author, update_author, delete_author
from author.views_author_role import ApiOverview as RoleOverview, add_author_to_movie, read_author_to_movie, read_detail_author_to_movie, update_author_to_movie, delete_author_to_movie

urlpatterns = [
    path('author/', AuthorReview, name='author_home'),
    path('author/create/', add_author, name='add_author'),
    path('author/list/', read_author, name='read_author'),
    path('author/read/<int:pk>/', read_detail_author.as_view(), name='book-detail'),
    path('author/update/<int:pk>/', update_author, name='update_author'),
    path('author/delete/<int:pk>/', delete_author, name='delete_author'),

    path('role/', RoleOverview, name='author_to_movie_home'),
    path('role/create/', add_author_to_movie, name='add_author_to_movie'),
    path('role/list/', read_author_to_movie, name='read_author_to_movie'),
    path('role/read/<int:pk>/', read_detail_author_to_movie.as_view(), name='read_author_to_movie'),
    path('role/update/<int:pk>/', update_author_to_movie, name='update_author_to_movie'),
    path('role/delete/<int:pk>/', delete_author_to_movie, name='delete_author_to_movie'),
]

# AuthorReview
# MovieReview