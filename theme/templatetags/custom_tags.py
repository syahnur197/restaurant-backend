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
        {'label': 'Dashboard', 'link' : reverse_lazy('dashboard_dashboard')},
        {'label': 'Branches', 'link' : reverse_lazy('dashboard_dashboard')},
        {'label': 'Products', 'link' : reverse_lazy('dashboard_product_list')},
        {'label': 'Orders', 'link' : reverse_lazy('dashboard_dashboard')},
        {'label': 'Setting', 'link' : reverse_lazy('dashboard_dashboard')},
    ]

    return {'navs' : navs}

@register.inclusion_tag('partials/_table.html')
def render_table(headers, records):
    return {
        'headers' : headers,
        'records' : records,
    }

@register.filter
def get_item(dictionary, key):
    return dictionary.__dict__.get(key)
