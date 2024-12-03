from django import forms

from application.models import Citizen
from application.models import User
from application.models import Report

from application.models import Blog


class CitizenForm(forms.ModelForm):
    class Meta:
        model = Citizen
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter your age'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'gender': forms.Select(attrs={'class': 'form-control'},
                                   choices=[('', 'Select your gender')] + list(Citizen.GENDER_CHOICES)),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'}),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*',
                'title': 'Upload image here'})
        }


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'}),

        }

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter your age'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'message': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your message'}),

        }


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your title'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'post': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your post'}),

        }


