from django.contrib import admin
from .models import Trip, TripDay, TripWaypoint


# Register your models here.
# admin.site.register(Trip)
# admin.site.register(TripDay)
# admin.site.register(TripWaypoint)


class TripAdmin(admin.ModelAdmin):
    list_display = ['trip_name', 'user', 'created_at', 'last_modified_at']
    list_filter = ['user', 'created_at']
    search_fields = ['trip_name']

class TripDayAdmin(admin.ModelAdmin):
    list_display = ['trip', 'day']
    list_filter = ['trip']
    search_fields = ['trip__trip_name']

class TripWaypointAdmin(admin.ModelAdmin):
    list_display = ['trip_day', 'waypoint_name', 'address', 'latitude', 'longitude', 'arrival_time', 'departure_time', 'duration']
    list_filter = ['trip_day']
    search_fields = ['waypoint_name']

admin.site.register(Trip, TripAdmin)
admin.site.register(TripDay, TripDayAdmin)
admin.site.register(TripWaypoint, TripWaypointAdmin)

