from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, 'dashboard/dashboard/index.html')
