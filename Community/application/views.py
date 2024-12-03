from django.contrib.auth import login
from django.shortcuts import render

from application.forms import CitizenForm

from application.forms import LoginForm

from application.forms import ReportForm

from application.forms import BlogForm


# Create your views here.
def index(request):
    return render(request, 'index.html')

def settings(request):
    return render(request, 'settings.html')

def about(request):
    return render(request, 'about.html')


def register(request):
    form = CitizenForm()
    return render(request, 'register.html', {'form': form})


def report(request):
    report = ReportForm()
    return render(request, 'report.html', {"report": report} )


def login(request):
    login = LoginForm()
    return render(request, 'login.html', {'login': login} )

def blog(request):
    post = BlogForm
    return render(request, 'blog.html', {'post': post})




