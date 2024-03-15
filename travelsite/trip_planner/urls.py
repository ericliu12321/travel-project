from django.urls import path
from .views import testrenderTemplate, renderTravelDetails

urlpatterns = [
    path('testTemplate/', testrenderTemplate, name='testrenderTemplate'),
    path('testTravelDetails/', renderTravelDetails, name='renderTravelDetails'),
]
