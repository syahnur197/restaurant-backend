from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard_dashboard'),
    path('products/', views.ProductListView.as_view(), name='dashboard_product_list'),
    path('products/create', views.ProductCreateView.as_view(), name='dashboard_product_create'),
    path('products/<pk>', views.ProductUpdateView.as_view(), name='dashboard_product_update'),
    path('branches/', views.BranchListView.as_view(), name='dashboard_branch_list'),
    path('branches/<pk>/', views.BranchUpdateView.as_view(), name='dashboard_branch_update'),
    path('branches/<pk>/opening-hours/create', views.OpeningHourCreateView.as_view(), name='dashboard_opening_hour_create'),
    path('branches/<pk>/opening-hours/', views.OpeningHourListView.as_view(), name='dashboard_opening_hour_list'),
    path('branches/<pk>/opening-hours/<opening_hour_id>', views.OpeningHourUpdateView.as_view(), name='dashboard_opening_hour_update'),
]
