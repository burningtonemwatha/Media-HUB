from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate # Django inbuilt operation that return true or false
from django.contrib.auth.decorators import login_required # Returns true or false -> gives permission to usage of view actions based
# off user login activities # Decorators : functions return other functions
from django.contrib import messages
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from django.urls import reverse_lazy
from .forms import UserRegistrationForm, UserLoginForm, UserProfileForm
# Create your views here.

# Create your views here

def register_view(request):
    # validate if the user is alreday authenticated
    if request.user.is_authenticated:
        return redirect('mdedia_assets:dashboard')
    
    if request.method == 'POST': # User wants to register
        form = UserRegistrationForm(request.POST)
        # If user has filled in all requred inputs
        if form.is_valid():
            user = form.save() # Submits our user to our db
            login(request,user) # Call the login action
            messages.success(request, f'Welcome {user.username}! Your account has been successfully created!')
            return redirect('media_assets:dashboard')
        else:
            form = UserRegistrationForm() # Default HTTP Method is GET
        return render(request, 'accounts/register.html', {'form', form})

# Login View

def login_view(request):
    # validate if the user is alreday authenticated
    if request.user.is_authenticated:
        return redirect('mdedia_assets:dashboard')
    
    if request.method == 'POST': # User wants to register
        form = UserLoginForm(request.POST)
        # If user has filled in all requred inputs
        if form.is_valid():
            # Pick up entries for username and passwords
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            #Djangomethod authenticate to aunthenticate  and login my user
            user = authenticate(username, password) # quesries the db looking for the user with mentioned credentials

            # Is the user found not in db
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back {username}')
                return redirect('media_assets:dashboard')
        else:
            form = UserRegistrationForm() # Default HTTP Method is GET
        return render(request, 'accounts/login.html', {'form', form})