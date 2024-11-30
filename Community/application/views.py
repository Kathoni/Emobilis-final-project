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

def report_crime(request):
    if request.method == "POST":
        form = CrimeReportForm(request.POST)
        if form.is_valid():
            crime_report = form.save(commit=False)
            crime_report.user = request.user  # Link the report to the logged-in user
            crime_report.save()
            return redirect('index')  # Redirect after successful crime report submission
    else:
        form = CrimeReportForm()
    return render(request, 'crime/report_crime.html', {'form': form})

def crime_reports(request):
    reports = CrimeReport.objects.all()  # You could filter this by the user's location
    return render(request, 'crime/crime_reports.html', {'reports': reports})