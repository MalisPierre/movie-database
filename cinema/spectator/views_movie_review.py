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
        'Overview MovieReview': '/',
        'Read MovieReview': '/read',
        'Add MovieReview': '/create',
        'Update MovieReview': '/update/pk',
        'Delete MovieReview': '/delete/pk'
    }

    return Response(api_urls)


# -------------------------------------------------------
# ----------------------- CREATE ------------------------
# -------------------------------------------------------
# @api_view(['POST'])
# @authentication_classes([JWTAuthentication])
# @permission_classes([IsAuthenticated])
# def add_movie_review(request):
#     movie_review = MovieReviewSerializer(data=request.data)

#     if MovieReview.objects.filter(**request.data).exists():
#         raise serializers.ValidationError('This data already exists')

#     if movie_review.is_valid():
#         movie_review.save()
#         return Response(movie_review.data)
#     else:
#         return Response(status=status.HTTP_404_NOT_FOUND)

class add_movie_review(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = MovieReviewSerializer(data=request.data)

        if MovieReview.objects.filter(**request.data).exists():
            raise serializers.ValidationError('This data already exists')

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

# -------------------------------------------------------
# ----------------------- READ --------------------------
# -------------------------------------------------------
@api_view(['GET'])
def read_movie_review(request):
    movie_reviews = MovieReview.objects.all()

    if movie_reviews:
        serializer = MovieReviewSerializer(movie_reviews, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

    

# -------------------------------------------------------
# ----------------------- UPDATE ------------------------
# -------------------------------------------------------
@api_view(['POST'])
def update_movie_review(request, pk):
    user_id = request.user.id
    movie_review = MovieReview.objects.get(pk=pk)
    if movie_review.user.id != user_id:
        return Response(status=status.HTTP_403_FORBIDDEN)
    data = MovieReviewSerializer(instance=movie_review, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
# -------------------------------------------------------
# ----------------------- DELETE ------------------------
# -------------------------------------------------------
@api_view(['DELETE'])
def delete_movie_review(request, pk):
    movie_review = get_object_or_404(MovieReview, pk=pk)
    movie_review.delete()
    return Response(status=status.HTTP_202_ACCEPTED)