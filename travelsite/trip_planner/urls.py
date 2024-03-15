from django.urls import path
from .views import testrenderTemplate

urlpatterns = [
    path('testTemplate/', testrenderTemplate, name='testrenderTemplate'),
]
