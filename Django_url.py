# urls.py
from django.urls import path
from . import Django_views

urlpatterns = [
    path('', Django_views.home),
]
