from django.shortcuts import render

BASE_DIR = 'dashboard/'

def dashboard(request):
    return render(request, template_name=BASE_DIR + 'dashboard/index.html')
