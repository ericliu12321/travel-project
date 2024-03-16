from django.urls import path
# from .views import testrenderTemplate, renderTravelDetails, renderTripStop, renderTripDay
from .views import *

urlpatterns = [
    path('testTemplate/', testrenderTemplate, name='testrenderTemplate'),
    path('testTravelDetails/', renderTravelDetails, name='renderTravelDetails'),
    path('testTripStop/', renderTripStop, name='renderTripStop'),
    path('testTripDay/', renderTripDay, name='renderTripDay'),
]
