# vyreon\views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm
from vyreon.formsmodel import EditProfileForm
from django.contrib.auth.forms import UserCreationForm


def index(request):
    context = {
        'sidecontent': True,
    }
    return render(request, 'index.html', context)


@login_required
def profile(request):
    context = {
        'sidecontent': True,
    }
    return render(request, 'profile.html', context)


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = EditProfileForm(instance=request.user)
    return render(request, 'edit_profile.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})