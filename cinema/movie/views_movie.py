from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import serializers, status, generics
from rest_framework.views import APIView
from movie.models import Movie
from movie.serializers import MovieSerializer, MovieDetailSerializer
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
        'Overview Movie': '/',
        'List Movie': '/list',
        'Read Movie': '/read/pk',
        'Add Movie': '/create',
        'Update Movie': '/update/pk',
        'Delete Movie': '/delete/pk'
    }

    return Response(api_urls)


# -------------------------------------------------------
# ----------------------- CREATE ------------------------
# -------------------------------------------------------
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_movie(request):
    movie = MovieSerializer(data=request.data)

    if Movie.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')

    if movie.is_valid():
        movie.save()
        return Response(movie.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

# -------------------------------------------------------
# ----------------------- LIST --------------------------
# -------------------------------------------------------
class read_movie(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        if movies:
            serializer = MovieSerializer(movies, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        from django.db.models import Q
        import re
        data = request.data
        publishedDateStart = request.data.get('publishedDateStart')
        publishedDateEnd = request.data.get('publishedDateEnd')
        genres = request.data.get('genre')
        statusses = request.data.get('status')
        movies = Movie.objects.all()
        if publishedDateStart:
            movies = movies.filter(release_date__gt=publishedDateStart)
        if publishedDateEnd:
            movies = movies.filter(release_date__lt=publishedDateEnd)
        if genres:
            movies = movies.filter(genre__in=genres)
            # regex = r'(^|,)(' + '|'.join(re.escape(val) for val in genres) + r')(,|$)'
            # movies = movies.filter(genre__regex=regex)
        if statusses:
            movies = movies.filter(status__in=statusses)
        if movies:
            serializer = MovieSerializer(movies, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

# -------------------------------------------------------
# ----------------------- READ --------------------------
# -------------------------------------------------------
class read_detail_movie(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializer
    

# -------------------------------------------------------
# ----------------------- UPDATE ------------------------
# -------------------------------------------------------
@api_view(['POST'])
def update_movie(request, pk):
    movie = Movie.objects.get(pk=pk)
    data = MovieSerializer(instance=movie, data=request.data, partial=True)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
# -------------------------------------------------------
# ----------------------- DELETE ------------------------
# -------------------------------------------------------
@api_view(['DELETE'])
def delete_movie(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    movie.delete()
    return Response(status=status.HTTP_202_ACCEPTED)