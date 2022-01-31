from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from authentication.mixins import HasRestaurantMixin
from restaurant.models import Branch, Product, Restaurant


class DashboardView(LoginRequiredMixin, HasRestaurantMixin, TemplateView):
    template_name = 'dashboard/dashboard/index.html'

class ProductListView(LoginRequiredMixin, HasRestaurantMixin, ListView):
    template_name = "dashboard/product/product-list.html"
    context_object_name = "products"

    def get_queryset(self):
        user_restaurant = self.request.user.getUserRestaurant()
        return Product.objects.filter(restaurant=user_restaurant)


class BranchListView(LoginRequiredMixin, HasRestaurantMixin, ListView):
    model = Branch
    template_name = "dashboard/branch/branch-list.html"
    context_object_name = "branches"
