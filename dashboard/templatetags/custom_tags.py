import datetime
from django import template
from django.urls import reverse_lazy
from src import settings

register = template.Library()

@register.simple_tag(name='current_time')
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)

@register.inclusion_tag('partials/_sidebar.html')
def show_sidebar():
    navs = [
        {'label': 'Dashboard', 'link' : reverse_lazy('dashboard_dashboard')},
        {'label': 'Branches', 'link' : reverse_lazy('dashboard_branch_list')},
        {'label': 'Products', 'link' : reverse_lazy('dashboard_product_list')},
        # {'label': 'Orders', 'link' : reverse_lazy('dashboard_dashboard')},
        {'label': 'Setting', 'link' : reverse_lazy('dashboard_setting')},
    ]

    return {'navs' : navs}

@register.inclusion_tag('partials/_table.html')
def render_table(headers, records):
    return {
        'headers' : headers,
        'records' : records,
    }

@register.inclusion_tag('partials/_javascript.html')
def render_javascript():
    return {
        'petite_vue' : settings.PETITE_VUE_URL,
    }

@register.filter
def get_item(dictionary, key):
    returned_value = dictionary.__dict__.get(key)
    if returned_value is None:
        return ''
    return returned_value

@register.filter
def call_method(record, func):
    return getattr(record, func)()
