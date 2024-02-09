# main_app/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserForm, ProfileForm
from .models import Profile

def edit_profile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=profile)
    return render(request, 'edit_profile.html', {'user_form': user_form, 'profile_form': profile_form})

def resume(request):
    # Logic to serve the resume file, or generate it dynamically
    # For simplicity, let's assume you have a static file for the resume
    return redirect('/path/to/your/resume.pdf')
