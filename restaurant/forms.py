from django.forms import ModelForm, RadioSelect, TextInput, Textarea, TimeInput
from restaurant.models import Branch, OpeningHour, Product, Restaurant
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit


class RestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        fields = (
            'name',
            'description',
            'phone_number',
            'cuisines',
            'facebook',
            'instagram',
            'twitter',
            'website',
            'email',
            'origin_country',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'flex flex-col space-y-4'
        self.helper.form_tag = False
        self.helper.layout = Layout(
            'name',
            'description',
            'cuisines',
            Div(
            'facebook',
            'instagram',
            'twitter',
            'website',
            css_class='grid grid-cols-4 gap-2'
            ),
            Div(
            'email',
            'phone_number',
            css_class='grid grid-cols-2 gap-2'
            ),
            'origin_country',
            Submit('submit', 'Submit', css_class='bg-blue-200 w-1/4 py-4 rounded-md text-blue-800 hover:bg-blue-400 hover:text-blue-900')
        )

class BranchForm(ModelForm):
    class Meta:
        model = Branch
        fields = (
            'name',
            'address',
            'phone_number',
            'payment_instruction',
        )
        widgets = {
            'payment_instruction': Textarea(attrs={'rows': 5}),
        }
        help_texts = {
            'payment_instruction': 'You may list down all the payment methods you offer and their instructions',
        }

    def clean_country(self):
        return "BN"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'flex flex-col space-y-4'
        self.helper.form_tag = False
        self.helper.layout = Layout(
            'name',
            'address',
            'phone_number',
            'payment_instruction',
        )

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'unit_price', 'status', 'photo',)
        widgets = {
            'status': RadioSelect(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'flex flex-col space-y-4'
        self.helper.layout = Layout(
            'name',
            'description',
            'unit_price',
            'status',
            'photo',
            Submit('submit', 'Submit', css_class='bg-blue-200 w-1/4 py-4 rounded-md text-blue-800 hover:bg-blue-400 hover:text-blue-900')
        )


class OpeningHourForm(ModelForm):
    class Meta:
        model = OpeningHour
        fields = (
            'days',
            'start_time',
            'end_time',
            'break_start_time',
            'break_end_time',
        )

        widgets = {
            'days' : TextInput(attrs={'value' : 'Monday-Thursday'}),
            'start_time': TimeInput(attrs={'type': 'time', 'value': '10:00'}),
            'end_time': TimeInput(attrs={'type': 'time', 'value': '22:00'}),
            'break_start_time': TimeInput(attrs={'type': 'time'}),
            'break_end_time': TimeInput(attrs={'type': 'time'}),
        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'flex flex-col space-y-4'
        self.helper.layout = Layout(
            'days',
            'start_time',
            'end_time',
            'break_start_time',
            'break_end_time',
            Submit('submit', 'Submit', css_class='cursor-pointer bg-blue-200 w-1/4 py-4 rounded-md text-blue-800 hover:bg-blue-400 hover:text-blue-900')
        )
