from django.urls import reverse_lazy


def get_dashboard_breadcrumbs():
    return [
        {'link' : reverse_lazy('dashboard_dashboard'), 'label' : 'Dashboard'},
        {'link' : reverse_lazy('dashboard_dashboard'), 'label' : 'Home'},
    ]

def get_branch_list_breadcrumbs():
    return [
        {'link' : reverse_lazy('dashboard_dashboard'), 'label' : 'Dashboard'},
        {'link' : reverse_lazy('dashboard_branch_list'), 'label' : 'Branches'},
    ]

def get_product_list_breadcrumbs():
    return [
        {'link' : reverse_lazy('dashboard_dashboard'), 'label' : 'Dashboard'},
        {'link' : reverse_lazy('dashboard_product_list'), 'label' : 'Products'},
    ]
