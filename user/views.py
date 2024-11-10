from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm
from django.contrib import messages

# Create your views here.


def register(request):
    if request.method == 'POST':
       form = CreateUserForm(request.POST)
       if form.is_valid():
            form.save()
            return redirect('user-login')
    else:
        form = CreateUserForm()
    context = {
        'form': form,
    }
    return render(request, 'user/register.html', context)

def custom_logout(request):
    logout(request)
    return redirect('user-logout')  # Redirect to login page after logout