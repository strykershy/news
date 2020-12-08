from django.contrib import admin
from . import views
from .views import signup
from django.urls import path

urlpatterns = [
    path('',  signup, name='signup'),
]