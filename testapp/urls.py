from django.urls import path
from . import views

urlpatterns = [
    path('',views.location_generator,name="ipstack"),
]