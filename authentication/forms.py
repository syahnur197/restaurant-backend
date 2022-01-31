from django.forms import CharField, TextInput, ModelForm
from django.utils.translation import gettext_lazy as _

from allauth.account.forms import LoginForm, SignupForm

from restaurant.models import Restaurant, UserProfile

class CustomLoginForm(LoginForm):

    def login(self, *args, **kwargs):

        # Add your own processing here.

        # You must return the original result.
        return super(CustomLoginForm, self).login(*args, **kwargs)

class CustomSignupForm(SignupForm):
    full_name = CharField(
        label=_("Full Name"),
        max_length=100,
        widget=TextInput(
            attrs={"placeholder": _("Full Name"), "autocomplete": "fullname"}
        ),
    )

    def save(self, request):

        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super(CustomSignupForm, self).save(request)

        full_name = self.cleaned_data.get('full_name')
        UserProfile.objects.create(full_name=full_name, user=user)

        # You must return the original result.
        return user

class SetupRestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        exclude = ('creator',)
