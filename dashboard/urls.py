from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard_dashboard'),
    path('products/', views.ProductListView.as_view(), name='dashboard_product_list'),
    path('products/create', views.ProductCreateView.as_view(), name='dashboard_product_create'),
    path('branches/', views.BranchListView.as_view(), name='dashboard_branch_list'),
]
