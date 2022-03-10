from dataclasses import field
from pyexpat import model
from django import forms
from .models import User, Post

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password']
        # widgets = {'passward':forms.PasswordInput}

class UserLoginForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','password']
        