from django.forms import CheckboxSelectMultiple, ModelForm, Textarea

from restaurant.models import Branch, Restaurant
from allauth.account.forms import SignupForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML


class CustomSignUpForm(SignupForm):
    pass

class SetUpRestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        fields = (
            'name',
            'description',
            'phone_number',
            'cuisine_types',
            'meal_types',
            'dining_types',
        )
        widgets = {
            'description': Textarea(attrs={'rows': 5}),
            'cuisine_types': CheckboxSelectMultiple(),
            'meal_types': CheckboxSelectMultiple(),
            'dining_types': CheckboxSelectMultiple(),
        }

    def clean_origin_country(self):
        return "BN"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'flex flex-col space-y-4'
        self.helper.layout = Layout(
            'name',
            'description',
            'phone_number',
            HTML('<h3 class="mt-8 text-lg font-bold text-gray-700">Types</h3>'),
            HTML('<p class="text-gray-700 mb-2">Please select your food types</p>'),
            Div(
                'cuisine_types',
                'meal_types',
                'dining_types',
                css_class='grid grid-cols-3 gap-2',
            ),
            Submit('submit', 'Submit', css_class='cursor-pointer bg-blue-200 w-1/4 py-4 rounded-md text-blue-800 hover:bg-blue-400 hover:text-blue-900'),
        )

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
