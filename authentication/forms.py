from django.forms import ModelForm

from restaurant.models import Branch, Restaurant

class SetUpRestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        fields = (
            'name',
            'description',
            'phone_number',
            'cuisines',
            'origin_country',
        )

class SetUpBranchForm(ModelForm):
    class Meta:
        model = Branch
        fields = (
            'name',
            'address',
            'phone_number',
            'country',
            'latitude',
            'longitude',
        )
