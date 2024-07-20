# bookings/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LocationViewSet, HotelViewSet, RoomViewSet, BookingViewSet, AboutViewSet

router = DefaultRouter()
router.register(r'locations', LocationViewSet)
router.register(r'hotels', HotelViewSet)
router.register(r'rooms', RoomViewSet)
router.register(r'bookings', BookingViewSet)
router.register(r'abouts', AboutViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
