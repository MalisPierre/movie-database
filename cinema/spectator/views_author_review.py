from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.views import APIView
from spectator.models import AuthorReview
from spectator.serializers import AuthorReviewSerializer
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404

# -------------------------------------------------------
# ----------------------- OVERVIEW ----------------------
# -------------------------------------------------------
@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'Overview AuthorReview': '/',
        'Read AuthorReview': '/read',
        'Add AuthorReview': '/create',
        'Update AuthorReview': '/update/pk',
        'Delete AuthorReview': '/delete/pk'
    }

    return Response(api_urls)


# -------------------------------------------------------
# ----------------------- CREATE ------------------------
# -------------------------------------------------------
@api_view(['POST'])
def add_author_review(request):
    author_review = AuthorReviewSerializer(data=request.data)

    if AuthorReview.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')

    if author_review.is_valid():
        author_review.save()
        return Response(author_review.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

# -------------------------------------------------------
# ----------------------- READ --------------------------
# -------------------------------------------------------
@api_view(['GET'])
def read_author_review(request):
    author_reviews = AuthorReview.objects.all()

    if author_reviews:
        serializer = AuthorReviewSerializer(author_reviews, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

    

# -------------------------------------------------------
# ----------------------- UPDATE ------------------------
# -------------------------------------------------------
@api_view(['POST'])
def update_author_review(request, pk):
    author_review = AuthorReview.objects.get(pk=pk)
    data = AuthorReviewSerializer(instance=author_review, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
# -------------------------------------------------------
# ----------------------- DELETE ------------------------
# -------------------------------------------------------
@api_view(['DELETE'])
def delete_author_review(request, pk):
    author_review = get_object_or_404(AuthorReview, pk=pk)
    author_review.delete()
    return Response(status=status.HTTP_202_ACCEPTED)