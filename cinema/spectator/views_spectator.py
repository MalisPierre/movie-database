from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.views import APIView
from spectator.models import Spectator
from spectator.serializers import SpectatorSerializer
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404

# -------------------------------------------------------
# ----------------------- OVERVIEW ----------------------
# -------------------------------------------------------
@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'Overview Spectators': '/',
        'Read Spectators': '/read',
        'Add Spectators': '/create',
        'Update Spectators': '/update/pk',
        'Delete Spectators': '/delete/pk'
    }

    return Response(api_urls)


# -------------------------------------------------------
# ----------------------- CREATE ------------------------
# -------------------------------------------------------
#{"email": "test@gmail.com","first_name": "test","last_name": "test","is_active": true,"is_staff": false, "username": "test", "password": "test"}
@api_view(['POST'])
def add_spectator(request):
    serializer = SpectatorSerializer(data=request.data)

    if Spectator.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

# -------------------------------------------------------
# ----------------------- READ --------------------------
# -------------------------------------------------------
@api_view(['GET'])
def read_spectator(request):
    spectators = Spectator.objects.all()

    if spectators:
        serializer = SpectatorSerializer(spectators, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

    

# -------------------------------------------------------
# ----------------------- UPDATE ------------------------
# -------------------------------------------------------
@api_view(['POST'])
def update_spectator(request, pk):
    spectator = Spectator.objects.get(pk=pk)
    serializer = SpectatorSerializer(instance=spectator, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
# -------------------------------------------------------
# ----------------------- DELETE ------------------------
# -------------------------------------------------------
@api_view(['DELETE'])
def delete_spectator(request, pk):
    spectator = get_object_or_404(Spectator, pk=pk)
    spectator.delete()
    return Response(status=status.HTTP_202_ACCEPTED)