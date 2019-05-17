from django import forms
from .models import Board
from django.forms import ModelForm
from django.contrib.auth.models import User

class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['title', 'body']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']