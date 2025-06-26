from django.db.models import fields
from rest_framework import serializers
from author.models import Author, AuthorToMovie
from spectator.serializers import AuthorReviewSerializer


class AuthorToMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorToMovie
        fields = ('id', 'author', 'movie', 'role')
        read_only_fields = ['id']

class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ('id', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'birthday')
        read_only_fields = ['id']


class AuthorDetailSerializer(serializers.ModelSerializer):

    notes = AuthorReviewSerializer(
        source='authorReviews',
        many=True,
        read_only=True
    )

    class Meta:
        model = Author
        fields = ('id', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'birthday', 'average_note', 'notes', 'movies')
        read_only_fields = ['id', 'average_note', 'notes']