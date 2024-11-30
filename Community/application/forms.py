from django import forms

from application.models import Citizen
from django.contrib.auth.forms import UserCreationForm

from application.models import CrimeReport


class CitizenForm(forms.ModelForm):
    class Meta:
        model = Citizen
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter your age'}),
            'message': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your message'}),
            'gender': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your gender'}),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*',
                'title': 'Upload image here'})
        }


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Citizen
        fields = ['name', 'email', 'password1', 'password2']



class CrimeReportForm(forms.ModelForm):
    class Meta:
        model = CrimeReport
        fields = ['title', 'description', 'location']