from django.forms import ModelForm

from restaurant.models import Branch, Restaurant
from allauth.account.forms import SignupForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field


class CustomSignUpForm(SignupForm):
    pass

class SetUpRestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        fields = (
            'name',
            'description',
            'phone_number',
            'cuisines',
        )

    def clean_origin_country(self):
        return "BN"

class SetUpBranchForm(ModelForm):
    class Meta:
        model = Branch
        fields = (
            'name',
            'address',
            'phone_number',
        )

    def clean_country(self):
        return "BN"
