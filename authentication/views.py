from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from authentication.forms import SetupRestaurantForm

class SetUpRestaurantView(CreateView):
    """
    View to set up restaurant after sign up
    """
    template_name = 'account/restaurant.html'
    form_class = SetupRestaurantForm
    success_url = reverse_lazy('dashboard_dashboard')

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
