from django.urls import path, include
from . import views

urlpatterns = [
    path('restaurant', views.restaurant, name='authentication_restaurant'),
]
