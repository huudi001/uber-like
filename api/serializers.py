from rest_framework import serializers,viewsets
from app.models import *


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = '__all__'





class VehicleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vehicle
        fields = '__all__'
        depth = 1


class VehicleSerializerAdd(serializers.ModelSerializer):
    class Meta:
      model = Vehicle
      fields = '__all__'


class VehicleSharingSerializer(serializers.ModelSerializer):

    class Meta:
        model = VehicleSharing
        fields = '__all__'
        depth = 2


class VehicleSharingSerializerAdd(serializers.ModelSerializer):

    class Meta:
        model = VehicleSharing
        fields = '__all__'



class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
        depth = 2






class RequestSerializer(serializers.ModelSerializer):

    picture = serializers.CharField(source='user.profile.picture.url')
    user = UserSerializer()
    ride = VehicleSharingSerializer()
    class Meta:

        model = Request
        fields = ['id','pick','dest','reg_date','user','bearable','status','ride','picture']
        # fields = ['id','dest','reg_date','user','bearable','status','ride','picture']
        depth = 1
