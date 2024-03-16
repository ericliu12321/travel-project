"""
Module: views

Overview:
    This module implements all the views functionality that will be accessed
    from urls.

--------------------------------------------------------------------------------
"""
<<<<<<< Updated upstream
from .master_views import testrenderTemplate, renderTravelDetails, renderTripStop, renderTripDay
=======
from .master_views import testrenderTemplate, renderTravelDetails, my_trips, home_view, trip_view
from .account_views import signin_view, signup_view, logout_view
>>>>>>> Stashed changes

__all__ = [
    'signin_view',
    'signup_view',
    'home_view',
    'my_trips',
    'trip_view',
    'testrenderTemplate',
    'renderTravelDetails',
    'renderTripStop',
    'renderTripDay',
]