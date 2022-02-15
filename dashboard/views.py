from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, FormView
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from dashboard.headers import get_branch_list_headers, get_opening_hours_list_headers, get_product_list_headers
from dashboard.mixins import HasRestaurantMixin, UserRestaurantHasBranchMixin
from restaurant.forms import BranchForm, OpeningHourForm, ProductForm, RestaurantForm
from restaurant.models import Branch, OpeningHour, Product, Restaurant

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

class OpeningHourListView(MasterMixin, ListView):
    template_name = "dashboard/opening-hour/opening-hour-list.html"
    context_object_name = "records"

    def get_queryset(self):
        return OpeningHour.objects.filter(branch=self.kwargs['pk'])

    def render_to_response(self, context, **kwargs):
        context['headers'] = get_opening_hours_list_headers()
        context['branch'] = Branch.objects.filter(id=self.kwargs['pk']).first()

        user_restaurant = self.request.user.get_user_restaurant()

        if (context['branch'] is None):
            return redirect(reverse_lazy('dashboard_branch_list'))

        user_owns_branch = user_restaurant == context['branch'].restaurant

        if (not user_owns_branch):
            return redirect(reverse_lazy('dashboard_branch_list'))


        return super().render_to_response(context, **kwargs)

class OpeningHourCreateView(MasterMixin, CreateView):
    form_class = OpeningHourForm
    template_name =  "dashboard/opening-hour/opening-hour-create.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['branch'] = Branch.objects.filter(id=self.kwargs['pk']).first()
        return context

    def get_success_url(self):
        return reverse_lazy('dashboard_opening_hour_list', kwargs={'pk':self.kwargs['pk']})

    def form_valid(self, form):
        branch = Branch.objects.filter(id=self.kwargs['pk']).first()

        user_restaurant = self.request.user.get_user_restaurant()

        if (branch is None):
            return redirect(reverse_lazy('dashboard_branch_list'))

        user_owns_branch = user_restaurant == branch.restaurant

        if (not user_owns_branch):
            return redirect(reverse_lazy('dashboard_branch_list'))

        form.instance.branch = branch

        return super().form_valid(form)

class OpeningHourUpdateView(MasterMixin, UpdateView):
    form_class = OpeningHourForm
    template_name =  "dashboard/opening-hour/opening-hour-update.html"
    model = OpeningHour
    pk_url_kwarg = 'opening_hour_id'

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)

        user_restaurant = request.user.get_user_restaurant()

        if (user_restaurant != self.object.branch.restaurant):
            return redirect(reverse_lazy('dashboard_dashboard'))

        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['branch'] = Branch.objects.filter(id=self.kwargs['pk']).first()
        return context

    def get_success_url(self):
        return reverse_lazy('dashboard_opening_hour_list', kwargs={'pk':self.kwargs['pk']})

    def form_valid(self, form):
        branch = Branch.objects.filter(id=self.kwargs['pk']).first()

        user_restaurant = self.request.user.get_user_restaurant()

        if (branch is None):
            return redirect(reverse_lazy('dashboard_branch_list'))

        user_owns_branch = user_restaurant == branch.restaurant

        if (not user_owns_branch):
            return redirect(reverse_lazy('dashboard_branch_list'))

        form.instance.branch = branch

        return super().form_valid(form)

class Setting(MasterMixin, FormView):
    template_name = "dashboard/setting/restaurant-update.html"
    form_class = RestaurantForm
    success_url = reverse_lazy('dashboard_setting')


    def get_form(self, form_class=form_class):
        restaurant = self.request.user.get_user_restaurant()
        return form_class(instance=restaurant, **self.get_form_kwargs())

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

