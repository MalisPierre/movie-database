from django.db.models import fields
from rest_framework import serializers
from movie.models import Movie, MovieGenre

from spectator.serializers import MovieReviewSerializer

class MovieGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieGenre
        fields = ('id', 'name', 'remote_id')
        read_only_fields = ['id']


class MovieSerializer(serializers.ModelSerializer):
       
    class Meta:
        model = Movie
        fields = ('id', 'title', 'adult', 'budget', 'cover', 'release_date', 'status', 'genre')
        read_only_fields = ['id']

class MovieDetailSerializer(serializers.ModelSerializer):

    notes = MovieReviewSerializer(
        source='movieReviews',
        many=True,
        read_only=True
    )
    from author.serializers import AuthorToMovieSerializer   
    authors = AuthorToMovieSerializer(
        source='movies',
        many=True,
        read_only=True
    )
     
    class Meta:
        model = Movie
        fields = ('id', 'title', 'adult', 'budget', 'cover', 'release_date', 'status', 'genre', 'average_note', 'notes', 'authors')
        read_only_fields = ['id', 'average_note', 'notes', 'authors']

