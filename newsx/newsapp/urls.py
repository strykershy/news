from newsx import views
from django.urls.conf import path
from .views import signup

urlpatterns = [
    path('',  signup, name='signup'),
]