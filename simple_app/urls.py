from django.urls import path
from simple_app.views import *

urlpatterns = [
    path('home',home, name='home'),
    path('pal',pal, name='pal'),
]