from django.contrib import admin
from . import views
from .views import signup, home
from django.urls import path

urlpatterns = [
    path('',  home, name='index'),
    path('',  signup, name='signup'),
]
