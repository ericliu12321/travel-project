from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import SlugField

# Create your models here.
class Trip(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trip_name = models.CharField(max_length=100)
    trip_date = models.DateField()
    days = models.IntegerField()
    created_at = models.DateTimeField(auto_created=True)
    last_modified_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.trip_name

class TripDay(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    day = models.IntegerField() # Should increment depending on how many TripDay are in in the Trip

    def __str__(self) -> str:
        return f'{self.trip.trip_name} - Day {self.day}'

class TripWaypoint(models.Model):
    trip_day = models.ForeignKey(TripDay, on_delete=models.CASCADE)
    waypoint_name = models.CharField(max_length=200)
    address = models.CharField(max_length=255)  # Example field for storing address
    latitude = models.FloatField()              # Field for storing latitude
    longitude = models.FloatField()             # Field for storing longitude
    description = models.TextField()            # Field for storing description
    arrival_time = models.DateTimeField()       # Field for storing arrival time
    departure_time = models.DateTimeField()     # Field for storing departure time
    duration = models.DurationField()           # Field for storing duration