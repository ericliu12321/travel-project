"""
Module: trip_planner/urls.py

Overview:
    This module provides links for the entire trip_planner application.

Notes:
    We need some naming convension for the link names.

Naming Convesion:
    path: kebab-case/
    name: snake_case
--------------------------------------------------------------------------------
"""
# from .views import testrenderTemplate, renderTravelDetails, renderTripStop, renderTripDay
from .views import *
from django.urls import path, include
from .views import testrenderTemplate, renderTravelDetails, my_trips, home_view, trip_view, logout_view

urlpatterns = [
    # Landing Page
    path('', lambda temp: temp, name='main'),

    # Home Page (What the user sees when they login)
    path('home/', home_view, name='home'),

    # Profile/Settings
    path('accounts/', include('django.contrib.auth.urls'), name='login'),
    path('logout/', logout_view, name='logout'),

    # My Trips (Everything that has to do with trips)
    path('my-trips/', lambda temp: temp, name='my_trips'),
    path('my-trips/trip<int:trip_id>/', trip_view, name='trip_view'),
    path('my-trips/trip<int:trip_id>/manage/', trip_view, name='trip_manager'),

    path('test-template/', testrenderTemplate, name='test_template'),
    path('test-travel-details/', renderTravelDetails, name='test_travel_details'),
    path('test-trip-stop/', renderTripStop, name='test_trip_stop'),
    path('test-trip-day/', renderTripDay, name='test_trip_day'),

    # My Memories (Everything that has to do with past trips and photos)
    path('my-memories/', lambda temp: temp, name='my_memories'),
    path('my-memories/trip<int:trip_id>/', lambda temp: temp, name='my_memories'),

    # My Friends (Manage Friends and Groups)
    path('my-friends/', lambda temp: temp, name='my_friends'),
    path('my-friends/<str:friend_name><int:friend_id>/', lambda temp: temp, name='friend_view'),
]
