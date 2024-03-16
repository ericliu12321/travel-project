"""
Module: trip_planner/urls.py

Overview:
    This module provides links for the entire trip_planner application.

Notes:
    We need some naming convension for the link names.

Naming Convesion:
    path: kebab-case
    name: snake_case
--------------------------------------------------------------------------------
"""
# from .views import testrenderTemplate, renderTravelDetails, renderTripStop, renderTripDay
from .views import *
from django.urls import path, include
from .views import testrenderTemplate, renderTravelDetails, my_trips, home_view, trip_view, logout_view

urlpatterns = [
    path('', home_view, name='home-view'),
    path('accounts/', include('django.contrib.auth.urls'), name='login'),
    path('logout/', logout_view, name='logout'),
    path('accounts/profile/', my_trips, name='my_trips'),
    path('accounts/profile/trip<int:trip_id>/', trip_view, name='trip_view'),

    path('testTemplate/', testrenderTemplate, name='testrenderTemplate'),
    path('testTravelDetails/', renderTravelDetails, name='renderTravelDetails'),
    path('testTripStop/', renderTripStop, name='renderTripStop'),
    path('testTripDay/', renderTripDay, name='renderTripDay'),
]
