from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from ..models import Trip, TripDay, TripWaypoint

# Create your views here.

def testrenderTemplate(request):
    return render(request, 'trip_planner/testTemplate.html')

def renderTravelDetails(request):
    context = {
        'travelTime': '1 hour, 12 minutes'
    }
    return render(request, 'trip_planner/travelDetails.html', context)

def renderTripStop(request):
    context = {
        'waypointTitle': 'Stop Point 1',
        'waypointAddress': '56 Address Drive, City, State'
    }
    return render(request, 'trip_planner/tripStop.html', context)

def renderTripDay(request):
    context = {
        'waypoints': [
            {
                'waypointTitle': 'Stop Point 1',
                'waypointAddress': '56 Address Drive, City 1, State 1',
                'isFinal': False,
                'travelTime': '1 hour, 12 minutes'
            },
            {
                'waypointTitle': 'Stop Point 2',
                'waypointAddress': '78 Address Drive, City 2, State 2',
                'isFinal': True,
            }
        ]
    }
    return render(request, 'trip_planner/tripDay.html', context)
    return render(request, 'trip_planner/travelDetails.html')

def home_view(request):
    return render(request, 'trip_planner/home.html')

def my_trips(request):
    # Retrieve the current logged-in user from the request
    current_user = request.user
    user_trips = Trip.objects.filter(user=current_user)

    
    # Pass the current_user to the template context
    return render(request, 'trip_planner/my_trips.html', context={'user': current_user, 'trips': user_trips})

def trip_view(request, trip_id):
    trip = get_object_or_404(Trip.objects.filter(id=trip_id))

    return render(request, 'trip_planner/temp_trip_view.html', {'trip': trip})

