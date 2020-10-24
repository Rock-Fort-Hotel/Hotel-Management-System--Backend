from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets

#serializers
from .serializers import ReservationSerializer
from .serializers import RoomSerializer
from .serializers import (
CustomerSerializer,
reportSerializer,
confirmationSerializer,
outstandingSerializer
)



#models
from .models import reservation
from .models import room
from .models import (
customer,
report,
confirmation,
outstanding,
)

# Create your views here.


#test


class reportViewSet(viewsets.ModelViewSet):
    serializer_class = reportSerializer
    queryset = report.objects.all()

class confirmationViewSet(viewsets.ModelViewSet):
    serializer_class = confirmationSerializer
    queryset = confirmation.objects.all()

class outstandingViewSet(viewsets.ModelViewSet):
    serializer_class = outstandingSerializer
    queryset = outstanding.objects.all()




class outstandingViewSetStatus(viewsets.ModelViewSet):
    serializer_class = outstandingSerializer
    

    def get_queryset(self):
        queryset = outstanding.objects.all()
        return queryset

    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        print(params['pk'])
        tas = outstanding.objects.filter(out_status = params['pk'])
        serializer = outstandingSerializer(tas, many=True)
        return Response(serializer.data)

class confirmViewSetStatus(viewsets.ModelViewSet):
    serializer_class = confirmationSerializer
    

    def get_queryset(self):
        queryset = confirmation.objects.all()
        return queryset

    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        print(params['pk'])
        con = confirmation.objects.filter(con_status = params['pk'])
        serializer = confirmationSerializer(con, many=True)
        return Response(serializer.data)


