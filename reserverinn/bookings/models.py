from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Location(models.Model):
    CITY_CHOICES = [
        ('Nairobi', 'Nairobi'),
        ('Dubai', 'Dubai'),
        ('New York', 'New York'),
        ('London', 'London'),
        ('Berlin', 'Berlin'),
        ('Paris', 'Paris'),
    ]
    city = models.CharField(max_length=50, choices=CITY_CHOICES, null=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.city

class Hotel(models.Model):
    name = models.CharField(max_length=100, null=False)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    description = models.TextField()
    address = models.CharField(max_length=255, null=True)
    phone_number = PhoneNumberField(null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    photo = models.ImageField(upload_to='hotel_photos/', blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Room(models.Model):
    ROOM_TYPE_CHOICES = [
        ('Single', 'Single'),
        ('Double', 'Double'),
        ('Suite', 'Suite'),
    ]
    hotel = models.ForeignKey(Hotel, related_name='rooms', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='hotel_photos/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    room_type = models.CharField(max_length=50, choices=ROOM_TYPE_CHOICES)
    room_number = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.room_type} - {self.number}'

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, related_name='booking', null=True, blank=True, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Booking {self.id} by {self.user.username}'

class About(models.Model):
    title = models.CharField(max_length=100)
    hotel = models.OneToOneField(Hotel, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='hotel_photos/', blank=True, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title