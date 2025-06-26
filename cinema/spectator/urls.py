from django.urls import path
from spectator.views_spectator import ApiOverview as SpectatorOverview, add_spectator, read_spectator, update_spectator, delete_spectator
from spectator.views_author_review import ApiOverview as AuthorOverview, add_author_review, read_author_review, update_author_review, delete_author_review
from spectator.views_movie_review import ApiOverview as MovieOverview, add_movie_review, read_movie_review, update_movie_review, delete_movie_review

urlpatterns = [
    path('spectator/', SpectatorOverview, name='spectator_home'),
    path('spectator/create/', add_spectator, name='add_spectator'),
    path('spectator/read/', read_spectator, name='read_spectator'),
    path('spectator/update/<int:pk>/', update_spectator, name='update_spectator'),
    path('spectator/delete/<int:pk>/', delete_spectator, name='delete_spectator'),

    path('author_review/', AuthorOverview, name='author_review_home'),
    path('author_review/create/', add_author_review, name='add_author_review'),
    path('author_review/read/', read_author_review, name='read_author_review'),
    path('author_review/update/<int:pk>/', update_author_review, name='update_author_review'),
    path('author_review/delete/<int:pk>/', delete_author_review, name='delete_author_review'),

    path('movie_review/', MovieOverview, name='movie_review_home'),
    path('movie_review/create/', add_movie_review.as_view(), name='add_movie_review'),
    path('movie_review/read/', read_movie_review, name='read_movie_review'),
    path('movie_review/update/<int:pk>/', update_movie_review, name='update_movie_review'),
    path('movie_review/delete/<int:pk>/', delete_movie_review, name='delete_movie_review'),
]

# AuthorReview
# MovieReview