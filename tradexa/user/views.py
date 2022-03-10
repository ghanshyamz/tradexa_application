from email import message
from textwrap import fill
from django.shortcuts import redirect, render
from django.contrib import auth
from .form import UserLoginForm, UserRegisterForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        filled_form = UserRegisterForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            message = 'Successfully Registered'
        else:
            message = 'User already exist OR username is taken'
        new_form = UserRegisterForm()
        return render(request, 'register.html',{'registration_form':new_form, 'message':message})
    else:
        form = UserRegisterForm()
        return render(request, 'register.html',{'registration_form':form})

def login(request):
    if request.method == 'POST':
        filled_form = UserLoginForm(request.POST)
        # print(filled_form.is_valid())
        if True:
            username = filled_form.cleaned_data.get('username')
            password = filled_form.cleaned_data.get('password')
            print(username)
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect("post/")
            else:
                message = 'Login Failed'
                form = UserLoginForm()
                return render(request, 'login.html', {'login_form':form, 'message':message})
        else:
            print(filled_form.cleaned_data.get('password'))
            message = 'Enter valid data'
            form = UserLoginForm()
            return render(request, 'login.html', {'login_form':form, 'message':message})
    else:
        form = UserLoginForm()
        return render(request, 'login.html', {'login_form':form, 'message':''})

def logout(request):
    auth.logout(request)
    return redirect('/')

def post(request):
    pass