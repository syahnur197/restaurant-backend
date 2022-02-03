from django.forms import ModelForm, RadioSelect

from restaurant.models import Product
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Field
from crispy_forms.bootstrap import InlineRadios

class CreateProductForm(ModelForm):
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
            Submit('submit', 'Add', css_class='bg-blue-200 w-1/4 py-4 rounded-md text-blue-800 hover:bg-blue-400 hover:text-blue-900')
        )
