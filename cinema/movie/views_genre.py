from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers, status, generics
from rest_framework.views import APIView
from movie.models import MovieGenre
from movie.serializers import MovieGenreSerializer
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404

# -------------------------------------------------------
# ----------------------- OVERVIEW ----------------------
# -------------------------------------------------------
@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'Overview Genre': '/',
        'Read Genre': '/read',
        'Add Genre': '/create',
        'Update Genre': '/update/pk',
        'Delete Genre': '/delete/pk'
    }

    return Response(api_urls)


# -------------------------------------------------------
# ----------------------- CREATE ------------------------
# -------------------------------------------------------
@api_view(['POST'])
def add_movie_genre(request):
    movie_genre = MovieGenreSerializer(data=request.data)

    if MovieGenre.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')

    if movie_genre.is_valid():
        movie_genre.save()
        return Response(movie_genre.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

# -------------------------------------------------------
# ----------------------- LIST --------------------------
# -------------------------------------------------------
@api_view(['GET'])
def read_movie_genre(request):
    movie_genres = MovieGenre.objects.all()

    if movie_genres:
        serializer = MovieGenreSerializer(movie_genres, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

# -------------------------------------------------------
# ----------------------- READ --------------------------
# -------------------------------------------------------
class read_detail_movie_genre(generics.RetrieveAPIView):
    queryset = MovieGenre.objects.all()
    serializer_class = MovieGenreSerializer
    

# -------------------------------------------------------
# ----------------------- UPDATE ------------------------
# -------------------------------------------------------
@api_view(['POST'])
def update_movie_genre(request, pk):
    movie_genre = MovieGenre.objects.get(pk=pk)
    data = MovieGenreSerializer(instance=movie_genre, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
# -------------------------------------------------------
# ----------------------- DELETE ------------------------
# -------------------------------------------------------
@api_view(['DELETE'])
def delete_movie_genre(request, pk):
    movie_genre = get_object_or_404(MovieGenre, pk=pk)
    movie_genre.delete()
    return Response(status=status.HTTP_202_ACCEPTED)