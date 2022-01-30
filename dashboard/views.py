from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from restaurant.models import Branch, Product, Restaurant


@login_required
def dashboard(request):
    return render(request, 'dashboard/dashboard/index.html')

class ProductListView(LoginRequiredMixin, ListView):
    # model = Product
    template_name = "dashboard/product/product-list.html"
    context_object_name = "products"

    def get_queryset(self):
        user_restaurant = self.request.user.getUserRestaurant()
        return Product.objects.filter(restaurant=user_restaurant)


class BranchListView(LoginRequiredMixin, ListView):
    model = Branch
    template_name = "dashboard/branch/branch-list.html"
    context_object_name = "branches"
