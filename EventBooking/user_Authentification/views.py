from django.shortcuts import render, redirect
from django.contrib.auth import (
    authenticate,
    get_user_model,
    logout,
    login
)
from django.contrib.auth.forms import PasswordResetForm
from django.contrib import messages
from .forms import UserLoginForm, UserRegisterForm
from django.urls import reverse
from apartment.views import apartment_list 

def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect(reverse('apartment:apartment_list'))
    context = {
        'form': form
    }
    return render(request, 'signin.html', context)


def register_view(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect(reverse('apartment:apartment_list'))
    context = {
        'form': form
    }
    return render(request, 'signup.html', context)


def logout_view(request):
        logout(request)
        return render(request, 'logout.html')


def profile(request):
    return render(request, 'profile.html')


def password_reset(request):
    return render(request, 'password_reset.html')


# In views.py

# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from .forms import ProfileForm
# from .models import Profile
# from django.contrib.auth.models import User


# @login_required
# def create_or_update_profile(request):
#     try:
#         profile = request.user.profile
#         if request.method == 'POST':
#             form = ProfileForm(request.POST, request.FILES, instance=profile)
#             if form.is_valid():
#                 profile = form.save(commit=False)
#                 profile.is_profile_completed = True
#                 profile.save()
#                 return redirect('profile_detail')
#         else:
#             form = ProfileForm(instance=profile)
#         return render(request, 'profile_form.html', {'form': form})
#     except Profile.DoesNotExist:
#         if request.method == 'POST':
#             form = ProfileForm(request.POST, request.FILES)
#             if form.is_valid():
#                 profile = form.save(commit=False)
#                 profile.user = request.user
#                 profile.is_profile_completed = True
#                 profile.save()
#                 return redirect('profile_detail')
#         else:
#             form = ProfileForm()
#         return render(request, 'profile_form.html', {'form': form})
 
 
 
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .models import Profile
from django.contrib.auth.models import User

@login_required
def create_or_update_profile(request):
    try:
        # Attempt to get the user's profile
        profile = request.user.profile
        if request.method == 'POST':
            # If it's a POST request (form submission)
            form = ProfileForm(request.POST, request.FILES, instance=profile)
            if form.is_valid():
                # Save the form data to the profile
                profile = form.save(commit=False)
                profile.is_profile_completed = True
                profile.save()
                # Redirect to the 'profile_detail' view after successful form submission
                return redirect('user_Authentification:profile_detail')
        else:
            # For GET requests, display the form with the user's current profile data
            form = ProfileForm(instance=profile)
        return render(request, 'profile_form.html', {'form': form})

    except Profile.DoesNotExist:
        # If the user doesn't have a profile
        if request.method == 'POST':
            form = ProfileForm(request.POST, request.FILES)
            if form.is_valid():
                profile = form.save(commit=False)
                profile.user = request.user
                profile.is_profile_completed = True
                profile.save()
                return redirect('profile_detail')
            else:
                form = ProfileForm()
        return render(request, 'profile_form.html', {'form': form})

# def profile_detail(request):
#     profile = Profile.objects.get(user=request.user)
#     return render(request, 'profile_detail.html', {'profile': profile})



from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .models import Profile

@login_required
def profile_detail(request):
    try:
        profile = Profile.objects.get(user=request.user)
        return render(request, 'profile_detail.html', {'profile': profile})
    except Profile.DoesNotExist:
         return render(request, 'profile_detail.html')
