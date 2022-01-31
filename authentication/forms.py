from django.forms import ModelForm

from restaurant.models import Restaurant

class SetupRestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        exclude = ('creator',)
