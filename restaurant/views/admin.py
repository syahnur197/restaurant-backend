from django.shortcuts import render

def dashboard(request):
    return render(request, template_name='admin/dashboard/index.html')