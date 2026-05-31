from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from accounts.forms import RegisterForm, LoginForm


# Create your views here.

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request,'accounts/registration_page.html',{'form':form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('register')
            else:
                return redirect('product_list')
    else:
        form = LoginForm()
    return render(request,'accounts/login_page.html',{'form':form})

def logout_view(request):
    logout(request)
    return redirect('product_list')

@login_required
def profile_view(request):
    return render(request,'accounts/profile.html')