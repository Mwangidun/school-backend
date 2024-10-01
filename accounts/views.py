from django.shortcuts import render, redirect
from django.contrib import messages
from accounts.forms import UserSignUpForm
from django.contrib.auth import authenticate, login, logout
from accounts.models import CustomUser, Staff, Member
from django.views.generic import CreateView

def signup_view(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = "Member"
            user.save()
            # Save the Member profile
            member = Member(user=user)
            member.save()
            messages.success(request, 'Account created successfully')
            return redirect('/')
        else:
            messages.error(request, 'Form is not valid. Please check the errors below.')
    else:
        form = UserSignUpForm()

    context = {
        'form': form,
    }
    
    return render(request, 'sign_up.html', context)

def sign_in(request):
    if request.method == 'POST':
        email = request.POST['email']  # Use email instead of username
        password = request.POST['password']
        
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            if user.is_active:
                login(request, user)
                messages.success(request, 'Logged in successfully')
                return redirect('/')
            else:
                messages.error(request, 'Please activate your account')
                return redirect('/') 
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('/') 
            
    return render(request, 'login.html')  # Correct template name

def custom_logout(request):
    logout(request)
    return redirect('/')  # Redirect to the sign-in page
