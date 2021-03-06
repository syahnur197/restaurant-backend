from django.urls import path, include
from . import views

urlpatterns = [
    path('set-up-restaurant/', views.SetUpRestaurantView.as_view(), name='authentication_restaurant'),
    path('set-up-branch/', views.SetUpBranchView.as_view(), name='authentication_branch'),
]
