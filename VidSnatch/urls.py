from django.contrib import admin
from django.urls import path, include
from .views import twitter

urlpatterns = [
    path("twitter/", twitter, name="twitter"),  
]