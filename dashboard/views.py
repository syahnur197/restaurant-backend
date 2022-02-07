from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from dashboard.headers import get_branch_list_headers, get_product_list_headers
from dashboard.mixins import HasRestaurantMixin, UserRestaurantHasBranchMixin
from restaurant.forms import BranchForm, ProductForm
from restaurant.models import Branch, Product

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

class ProductUpdateView(MasterMixin, UpdateView):
    form_class = ProductForm
    template_name = "dashboard/product/product-update.html"
    success_url = reverse_lazy('dashboard_product_list')
    model = Product

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)

        user_restaurant = request.user.get_user_restaurant()

        if (user_restaurant != self.object.restaurant):
            return redirect(reverse_lazy('dashboard_dashboard'))

        return response

class ProductCreateView(MasterMixin, CreateView):
    form_class = ProductForm
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

class BranchUpdateView(MasterMixin, UpdateView):
    form_class = BranchForm
    template_name = "dashboard/branch/branch-update.html"
    success_url = reverse_lazy('dashboard_branch_list')
    queryset = Branch.objects

class Setting(MasterMixin, TemplateView):
    template_name = "dashboard/setting/setting.html"

