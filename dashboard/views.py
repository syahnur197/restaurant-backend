from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from dashboard.mixins import HasRestaurantMixin
from restaurant.models import Branch, Product


class DashboardView(LoginRequiredMixin, HasRestaurantMixin, TemplateView):
    template_name = 'dashboard/dashboard/index.html'

class ProductListView(LoginRequiredMixin, HasRestaurantMixin, ListView):
    template_name = "dashboard/product/product-list.html"
    context_object_name = "records"

    def get_queryset(self):
        user_restaurant = self.request.user.get_user_restaurant()
        return Product.objects.filter(restaurant=user_restaurant)

    def get_context_data(self,**kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['headers'] = [
            {
                'key': 'number',
                'label' : 'Number',
                'link' : '',
            },
            {
                'key': 'name',
                'label' : 'Product Name',
                'link' : 'edit_link',
            },
            {
                'key': 'description',
                'label' : 'Description',
                'link' : '',
            },
            {
                'key': 'status',
                'label' : 'Status',
                'link' : '',
            },
            {
                'key': 'edit',
                'label' : '',
                'link' : 'edit_link',
            },
        ]
        return context


class ProductCreateView(LoginRequiredMixin, HasRestaurantMixin, CreateView):
    model = Product
    template_name = "dashboard/product/product-create.html"
    fields = ('status', 'name', 'description', 'unit_price',)
    success_url = reverse_lazy('dashboard_product_list')

    def form_valid(self, form):
        form.instance.restaurant = self.request.user.user_profile.restaurant
        return super(ProductCreateView, self).form_valid(form)


class BranchListView(LoginRequiredMixin, HasRestaurantMixin, ListView):
    model = Branch
    template_name = "dashboard/branch/branch-list.html"
    context_object_name = "branches"
