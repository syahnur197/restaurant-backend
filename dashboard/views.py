from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from dashboard.mixins import HasRestaurantMixin
from restaurant.models import Branch, Product, Restaurant


class DashboardView(LoginRequiredMixin, HasRestaurantMixin, TemplateView):
    template_name = 'dashboard/dashboard/index.html'

class ProductListView(LoginRequiredMixin, HasRestaurantMixin, ListView):
    template_name = "dashboard/product/product-list.html"
    context_object_name = "products"

    def get_queryset(self):
        user_restaurant = self.request.user.getUserRestaurant()
        return Product.objects.filter(restaurant=user_restaurant)


class ProductCreateView(CreateView):
    model = Product
    template_name = "dashboard/product/product-create.html"


class BranchListView(LoginRequiredMixin, HasRestaurantMixin, ListView):
    model = Branch
    template_name = "dashboard/branch/branch-list.html"
    context_object_name = "branches"
