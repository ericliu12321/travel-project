from django.shortcuts import render

# Create your views here.

def testrenderTemplate(request):
    return render(request, 'trip_planner/testTemplate.html')

def renderTravelDetails(request):
    return render(request, 'trip_planner/travelDetails.html')