from django.shortcuts import render

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