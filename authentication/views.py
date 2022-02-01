from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from authentication.forms import SetUpBranchForm, SetUpRestaurantForm
from django.contrib.auth.mixins import LoginRequiredMixin

class SetUpRestaurantView(LoginRequiredMixin, CreateView):
    """
    View to set up restaurant after sign up
    """
    template_name = 'account/restaurant.html'
    form_class = SetUpRestaurantForm
    success_url = reverse_lazy('authentication_branch')

    def get(self, request, *args, **kwargs):
        if request.user.has_restaurant():
            return redirect(self.success_url)

        return super(SetUpRestaurantView, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.creator = self.request.user

        response = super(SetUpRestaurantView, self).form_valid(form)

        # assigning the restaurant to the user's profile
        restaurant = self.object
        self.request.user.user_profile.set_restaurant(restaurant)

        return response


class SetUpBranchView(LoginRequiredMixin, CreateView):
    """
    View to set up restaurant after sign up
    """
    template_name = 'account/branch.html'
    form_class = SetUpBranchForm
    success_url = reverse_lazy('dashboard_dashboard')

    def get_initial(self):
        """Return the initial data to use for forms on this view."""
        restaurant = self.request.user.user_profile.restaurant

        return {
            'country' : restaurant.origin_country,
            'phone_number' : restaurant.phone_number,
        }

    def form_valid(self, form):
        restaurant = self.request.user.user_profile.restaurant
        form.instance.restaurant = restaurant

        response = super(SetUpBranchView, self).form_valid(form)
        return response
