from allauth.account.forms import LoginForm

class CustomLoginForm(LoginForm):

    def login(self, *args, **kwargs):

        # Add your own processing here.

        # You must return the original result.
        return super(CustomLoginForm, self).login(*args, **kwargs)
