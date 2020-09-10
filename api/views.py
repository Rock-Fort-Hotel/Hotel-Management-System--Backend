from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

#serializers
from .serializers import ReservationSerializer
from .serializers import RoomSerializer

#models
from .models import reservation
from .models import room

# Create your views here.
@api_view(['GET'])
def get_api_url_patterns(request):
    api_urls = {
        'event-all': '/events',
        'users': '/users',
    }

#to get all the data in the table
@api_view(['GET'])
def Reservation(request):
    res = reservation.objects.all()
    serializer = ReservationSerializer(res, many=True)
    return Response(serializer.data)

#to fetch one row from the table using primary key
@api_view(['GET'])
def GetOneReservation(request, pk):
    getRes = reservation.objects.get(res_id=pk)
    serializer = ReservationSerializer(getRes, many=False)
    return Response(serializer.data)

#create new reservation
@api_view(['POST'])
def ReservationCreate(request):
    serializer = ReservationSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        new_data = serializer.data
        return Response(new_data)
    return Response(serializer.data)

#deleet the rsevation
@api_view(['DELETE'])
def ResDelete(request, pk):
    resdel = reservation.objects.get(res_id=pk)
    resdel.delete()
    return Response("deleted")

#res update
@api_view(['POST'])
def ResUpdate(request, pk):
    resupdate = reservation.objects.get(res_id=pk)
    serializer = ReservationSerializer(instance=resupdate, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        new_data = serializer.data
        return Response(new_data)
    return Response(serializer.data)

@api_view(['GET'])
def GetRooms(request):
    getRooms = room.objects.all()
    serializer = RoomSerializer(getRooms, many=True)
    return Response(serializer.data)