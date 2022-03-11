from email import message
from textwrap import fill
from django.shortcuts import redirect, render
from django.contrib import auth

from .models import Post
from .form import CreatePostForm, UserLoginForm, UserRegisterForm

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
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("post")
        else:
            message = 'Login Failed'
            form = UserLoginForm()
            return render(request, 'login.html', {'login_form':form, 'message':message})
    else:
        form = UserLoginForm()
        return render(request, 'login.html', {'login_form':form, 'message':''})

def logout(request):
    auth.logout(request)
    return redirect('login')

#TODO : convert GMT to IST OR show how much time passed after post
def post(request):
    queryset = Post.objects.order_by('-updated_at')# -updated_at for reverse order
    message = ''
    if request.method == 'POST':
        filled_form = CreatePostForm(request.POST)
        if filled_form.is_valid():
            instance = filled_form.save(commit=False)
            instance.user = request.user
            instance.save()
            # redirect('post')
        else:
            message = 'Not valid'
    post_form = CreatePostForm()
    return render(request, 'post.html',{'posts':queryset,'post_form':post_form, 'message':message})