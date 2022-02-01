from django.forms import ModelForm

from restaurant.models import Restaurant

class SetupRestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        exclude = ('status', 'activate_date', 'deactivate_date', 'creator', 'approved_at', 'rejected_at',)
