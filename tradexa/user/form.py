from dataclasses import field
from pyexpat import model
from django import forms
from .models import User, Post
from django.contrib.auth.forms import UserCreationForm

# class UserRegisterForm(forms.ModelForm):
#     # password = forms.CharField(widget=forms.PasswordInput)
#     class Meta:
#         model = User
#         fields = ['first_name','last_name','email','username','password']
#         # widgets = {'passward':forms.PasswordInput}

class UserRegisterForm(UserCreationForm):
	firstname = forms.CharField(required=True)
	lastname = forms.CharField(required=True)
	email = forms.EmailField(required=True)
	class Meta:
		model = User
		fields = ['firstname','lastname','email','username', 'password1', 'password2']

	def save(self, commit=True):
		user = super(UserRegisterForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class UserLoginForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','password']
        

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text']