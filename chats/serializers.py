from rest_framework import serializers
from .models import *


class RoomSerializers(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class MessageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['value', 'date', 'user', 'room']


