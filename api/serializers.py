from rest_framework import serializers
from .models import reservation
from .models import room
from .models import room_offer
from .models import (
customer,
report,
confirmation,
outstanding,

)


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



#jiniseroializers

class reportSerializer(serializers.ModelSerializer):
    class Meta:
        model = report
        fields = ['id','date','time','details','trans_id','amount']

class confirmationSerializer(serializers.ModelSerializer):
    class Meta:
        model = confirmation
        fields = ['id','con_date','con_time','con_details','con_trans_id','con_amount','con_status']

class outstandingSerializer(serializers.ModelSerializer):
    class Meta:
        model = outstanding
        fields = ['id','out_date','out_time','out_details','out_trans_id','out_amount','out_status']

