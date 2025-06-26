from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers, status, generics
from rest_framework.views import APIView
from author.models import AuthorToMovie
from author.serializers import AuthorToMovieSerializer
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404

# -------------------------------------------------------
# ----------------------- OVERVIEW ----------------------
# -------------------------------------------------------
@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'Overview Role': '/',
        'List Roles': '/list',
        'Read Roles': '/read/pk',
        'Create Role': '/create',
        'Update Role': '/update/pk',
        'Delete Role': '/delete/pk'
    }

    return Response(api_urls)


# -------------------------------------------------------
# ----------------------- CREATE ------------------------
# -------------------------------------------------------
#{"author": 2,"movie": 131,"role": "support"}
@api_view(['POST'])
def add_author_to_movie(request):
    author_to_movie = AuthorToMovieSerializer(data=request.data)

    if AuthorToMovie.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')

    if author_to_movie.is_valid():
        author_to_movie.save()
        return Response(author_to_movie.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

# -------------------------------------------------------
# ----------------------- LIST --------------------------
# -------------------------------------------------------
@api_view(['GET'])
def read_author_to_movie(request):
    author_to_movies = AuthorToMovie.objects.all()

    if author_to_movies:
        serializer = AuthorToMovieSerializer(author_to_movies, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

# -------------------------------------------------------
# ----------------------- READ --------------------------
# -------------------------------------------------------
class read_detail_author_to_movie(generics.RetrieveAPIView):
    queryset = AuthorToMovie.objects.all()
    serializer_class = AuthorToMovieSerializer
    

# -------------------------------------------------------
# ----------------------- UPDATE ------------------------
# -------------------------------------------------------
@api_view(['POST'])
def update_author_to_movie(request, pk):
    author_to_movie = AuthorToMovie.objects.get(pk=pk)
    data = AuthorToMovieSerializer(instance=author_to_movie, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
# -------------------------------------------------------
# ----------------------- DELETE ------------------------
# -------------------------------------------------------
@api_view(['DELETE'])
def delete_author_to_movie(request, pk):
    author_to_movie = get_object_or_404(AuthorToMovie, pk=pk)
    author_to_movie.delete()
    return Response(status=status.HTTP_202_ACCEPTED)