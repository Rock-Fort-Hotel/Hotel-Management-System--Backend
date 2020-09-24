from rest_framework import serializers
from .models import reservation
from .models import room
from .models import room_offer
from .models import customer

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = reservation
        fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = room
        fields = '__all__'

class RoomOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = room_offer
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = customer
        fields = '__all__'
