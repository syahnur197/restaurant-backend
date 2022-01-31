from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from authentication.forms import SetupRestaurantForm

from restaurant.models import Restaurant


class SetUpRestaurantView(CreateView):
    template_name = 'account/restaurant.html'
    form_class = SetupRestaurantForm

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        """
        Set the current user user_profile restaurant to the newly created
        """
        restaurant = self.object
        self.request.user.user_profile.setRestaurant(restaurant)
        return reverse_lazy('dashboard:dashboard')
