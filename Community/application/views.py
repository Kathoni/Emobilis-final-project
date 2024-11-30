from django.contrib.auth import login
from django.shortcuts import render, redirect

from application.forms import RegistrationForm, CrimeReportForm
from application.models import CrimeReport


# Create your views here.
def index(request):
    return render(request, 'index.html')

def settings(request):
    return render(request, 'settings.html')

def about(request):
    return render(request, 'about.html')


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')  # Redirect to the homepage after registration
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def report(request):
    if request.method == "POST":
        form = CrimeReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.user = request.user  # Link the report to the logged-in user
            report.save()
            return redirect('index')  # Redirect after successful crime report submission
    else:
        form = CrimeReportForm()
    return render(request, 'report/report.html', {'form': form})

def crimereports(request):
    reports = CrimeReport.objects.all()  # You could filter this by the user's location
    return render(request, 'crime/crimereports.html', {'reports': reports})

def blog(request):
    return render(request, 'blog.html')
