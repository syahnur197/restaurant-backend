from email.policy import default
from django import forms
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from dashboard.headers import get_branch_list_headers, get_product_list_headers
from dashboard.mixins import HasRestaurantMixin, UserRestaurantHasBranchMixin
from restaurant.forms import CreateProductForm
from restaurant.models import Branch, Product
from django_extensions.db.models import ActivatorModel
from django.forms.utils import ErrorList

class MasterMixin(LoginRequiredMixin, HasRestaurantMixin, UserRestaurantHasBranchMixin):
    pass


class DashboardView(MasterMixin, TemplateView):
    template_name = 'dashboard/dashboard/index.html'

class ProductListView(MasterMixin, ListView):
    template_name = "dashboard/product/product-list.html"
    context_object_name = "records"

    def get_queryset(self):
        user_restaurant = self.request.user.get_user_restaurant()
        return Product.objects.filter(restaurant=user_restaurant)

    def get_context_data(self,**kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['headers'] = get_product_list_headers()
        return context


class ProductCreateView(MasterMixin, CreateView):
    form_class = CreateProductForm
    template_name = "dashboard/product/product-create.html"
    success_url = reverse_lazy('dashboard_product_list')

    def form_valid(self, form):
        form.instance.restaurant = self.request.user.user_profile.restaurant
        return super(ProductCreateView, self).form_valid(form)


class BranchListView(MasterMixin, ListView):
    model = Branch
    template_name = "dashboard/branch/branch-list.html"
    context_object_name = "records"

    def get_queryset(self):
        user_restaurant = self.request.user.get_user_restaurant()
        return Branch.objects.filter(restaurant=user_restaurant)

    def get_context_data(self,**kwargs):
        context = super(BranchListView, self).get_context_data(**kwargs)
        context['headers'] = get_branch_list_headers()
        return context

class Setting(MasterMixin, TemplateView):
    template_name = "dashboard/setting/setting.html"

