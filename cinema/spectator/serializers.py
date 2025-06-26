from django.db.models import fields
from rest_framework import serializers
from spectator.models import Spectator, MovieReview, AuthorReview

class SpectatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spectator
        fields = ('id', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'avatar', 'password', 'username')
        read_only_fields = ['id']

    def create(self, validated_data):
        
        user = Spectator(**validated_data)
        if "password" in validated_data:
            user.set_password(validated_data['password'])
        user.save()
        return user
    
    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if "password" in validated_data:
            instance.set_password(validated_data['password'])
        instance.save()
        return instance

class AuthorReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorReview
        fields = ('id', 'user', 'author', 'note')
        read_only_fields = ['id']

class MovieReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieReview
        fields = ('id', 'user', 'movie', 'note')
        read_only_fields = ['id']