from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from src import settings

@login_required
def dashboard(request):
    return render(request, 'admin/dashboard/index.html', {
        'hello' : 'hello world'
    })
