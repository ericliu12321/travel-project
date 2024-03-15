"""
Module: views

Overview:
    This module implements all the views functionality that will be accessed
    from urls.

--------------------------------------------------------------------------------
"""
from .master_views import testrenderTemplate, renderTravelDetails

__all__ = [
    'testrenderTemplate',
    'renderTravelDetails',
]