from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _


from restaurant.models import Restaurant

class SetupRestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        exclude = ('creator',)
