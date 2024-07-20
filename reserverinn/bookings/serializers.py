from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Location, Hotel, Room, Booking, About

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'city']

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['id', 'name', 'location', 'description', 'address', 'phone_number', 'photo', 'email', 'created_at', 'updated_at']

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'hotel', 'photo', 'description', 'room_type', 'room_number', 'price', 'is_available']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'user', 'room', 'hotel', 'check_in', 'check_out', 'created_at', 'updated_at']

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ['id', 'title', 'hotel', 'description', 'photo', 'created_at', 'updated_at']