from django.shortcuts import redirect


class HasRestaurantMixin:
    """Verify that the current user has set up a restaurant."""
    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_restaurant():
            return redirect('authentication_restaurant')

        return super().dispatch(request, *args, **kwargs)
