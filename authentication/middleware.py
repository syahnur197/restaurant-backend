from django.shortcuts import redirect
from django.urls import resolve


class CompleteRegistrationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user

        if not user.is_authenticated:
            response = self.get_response(request)
            return response

        user_has_no_restaurant = not user.has_restaurant()

        if user_has_no_restaurant and not _currentUrlIsWhitelisted(request):
            return redirect('authentication_restaurant')

        response = self.get_response(request)
        return response

def _currentUrlIsWhitelisted(request):
    current_url = resolve(request.path_info).url_name

    whitelisted_urls_name = [
        'authentication_restaurant',
        'account_logout',
        'events',
    ]

    return current_url in whitelisted_urls_name
