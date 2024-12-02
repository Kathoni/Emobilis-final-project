from django.contrib.auth import login
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')

def settings(request):
    return render(request, 'settings.html')

def about(request):
    return render(request, 'about.html')


def register(request):
    return render(request, 'register.html')


