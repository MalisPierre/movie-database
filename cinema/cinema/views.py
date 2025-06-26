from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import serializers, status, generics
from rest_framework.views import APIView
from spectator.models import MovieReview
from spectator.serializers import MovieReviewSerializer
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

# -------------------------------------------------------
# ----------------------- OVERVIEW ----------------------
# -------------------------------------------------------
@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'Overview': '/home',
        'ADV': '/admin',
        'Author': '/author/author',
        'AuthorToRole': '/author/role',
        'Movie': '/movie/movie',
        'MovieGenre': '/movie/genre',
        'Spectator': '/spectator/spectator',
        'AuthorReview': '/spectator/author_review',
        'MovieReview': '/spectator/movie_review',
        'JWTokens': '/user/api/token/',
    }

    return Response(api_urls)