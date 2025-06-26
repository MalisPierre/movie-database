from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers, status, generics
from rest_framework.views import APIView
from author.models import Author
from author.serializers import AuthorSerializer, AuthorDetailSerializer
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404

# -------------------------------------------------------
# ----------------------- OVERVIEW ----------------------
# -------------------------------------------------------
@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'Overview Author': '/',
        'Read Authors': '/list',
        'Read Author': '/read/pk',
        'Add Author': '/create',
        'Update Author': '/update/pk',
        'Delete Author': '/delete/pk'
    }

    return Response(api_urls)


# -------------------------------------------------------
# ----------------------- CREATE ------------------------
# -------------------------------------------------------
#{"first_name":"Bradd", "last_name":"Pitt", "email":"braddpitt@gmail.com", "is_active": "True", "is_staff": "False", "birthday": "1980-01-24"}
@api_view(['POST'])
def add_author(request):
    author = AuthorSerializer(data=request.data)

    if len(request.data) == 0:
        raise serializers.ValidationError('No data received')
    if Author.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')

    if author.is_valid():
        author.save()
        return Response(author.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

# -------------------------------------------------------
# ----------------------- LIST --------------------------
# -------------------------------------------------------
@api_view(['GET'])
def read_author(request):
    authors = Author.objects.all()

    if authors:
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

# -------------------------------------------------------
# ----------------------- READ --------------------------
# -------------------------------------------------------
class read_detail_author(generics.RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorDetailSerializer
    

# -------------------------------------------------------
# ----------------------- UPDATE ------------------------
# -------------------------------------------------------
#{"first_name":"BraddEEE", "last_name":"Pitt", "email":"braddpitt@gmail.com", "is_active": "True", "is_staff": "False", "birthday": "1980-01-24"}
@api_view(['POST'])
def update_author(request, pk):
    author = Author.objects.get(pk=pk)
    data = AuthorSerializer(instance=author, data=request.data, partial=True)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
# -------------------------------------------------------
# ----------------------- DELETE ------------------------
# -------------------------------------------------------
@api_view(['DELETE'])
def delete_author(request, pk):
    author = get_object_or_404(Author, pk=pk)
    author.delete()
    return Response(status=status.HTTP_202_ACCEPTED)