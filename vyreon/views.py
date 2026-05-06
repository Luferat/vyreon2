# vyreon\views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from vyreon.formsmodel import EditProfileForm, RegisterForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


def index(request):
    context = {
        'sidecontent': True,
    }
    return render(request, 'index.html', context)


# Ver perfil do usuário logado
@login_required
def profile(request):
    context = {
        'sidecontent': True,
    }
    return render(request, 'user/profile.html', context)

# Editar perfil do usuário logado


@login_required
def edit_profile(request):
    if request.method == 'POST':
        print(request.POST)
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = EditProfileForm(instance=request.user)
    return render(request, 'user/edit_profile.html', {'form': form})


# Cadastro de novo usuário
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'user/register.html', {'form': form})


# Usuário logado altera a senha
@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # mantém o usuário logado
            return redirect('profile')
        else:
            print('>>> ERROS:', form.errors)
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'user/change_password.html', {'form': form})

# Remover conta
@login_required
def delete_account(request):
    if request.method == 'POST':
        request.user.delete()
        return redirect('home')
    return render(request, 'user/delete_account.html')
