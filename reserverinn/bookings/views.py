# bookings/views.py

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Location, Hotel, Room, Booking, About
from .serializers import LocationSerializer, HotelSerializer, RoomSerializer, BookingSerializer, AboutSerializer
from .permissions import IsAdminOrReadOnly, IsAuthenticatedAndOwner

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [IsAdminOrReadOnly]

class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = [IsAdminOrReadOnly]

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAdminOrReadOnly]

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [IsAuthenticatedAndOwner]
        return super().get_permissions()

class AboutViewSet(viewsets.ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
    permission_classes = [IsAdminOrReadOnly]