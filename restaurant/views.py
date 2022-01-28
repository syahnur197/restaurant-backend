from django.shortcuts import render

# Create your views here.

def getHomePage(request):
    return render(request, 'restaurant/index.html')
