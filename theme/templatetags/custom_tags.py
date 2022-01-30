import datetime
from django import template
from django.urls import reverse_lazy

register = template.Library()

@register.simple_tag(name='current_time')
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)

@register.inclusion_tag('partials/_sidebar.html')
def show_sidebar():
    navs = [
        {'label': 'Dashboard', 'link' : reverse_lazy('dashboard:dashboard')},
        {'label': 'Branches', 'link' : reverse_lazy('dashboard:dashboard')},
        {'label': 'Products', 'link' : reverse_lazy('dashboard:dashboard')},
        {'label': 'Orders', 'link' : reverse_lazy('dashboard:dashboard')},
        {'label': 'Setting', 'link' : reverse_lazy('dashboard:dashboard')},
    ]

    return {'navs' : navs}
