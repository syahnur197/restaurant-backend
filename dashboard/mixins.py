from django.shortcuts import redirect

from restaurant.models import Branch


class HasRestaurantMixin:
    """Verify that the current user has set up a restaurant."""
    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_restaurant():
            return redirect('authentication_restaurant')

        return super().dispatch(request, *args, **kwargs)

class UserRestaurantHasBranchMixin:
    """Verify that the current user has set up a branch."""
    def dispatch(self, request, *args, **kwargs):
        restaurant = request.user.user_profile.restaurant
        branches_count = Branch.objects.filter(restaurant=restaurant).count()

        if branches_count == 0:
            return redirect('authentication_branch')

        return super().dispatch(request, *args, **kwargs)
