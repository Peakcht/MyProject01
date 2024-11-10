from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.

#@login_required(login_url='user-login')

#@login_required
#@user_passes_test(lambda u: u.is_superuser)

@login_required(login_url='user-login')
def index(request):
    return render(request, 'dashboard/index.html')

@login_required(login_url='user-login')
def staff(request):
    return render(request, 'dashboard/staff.html')

@login_required(login_url='user-login')
def product(request):
    return render(request, 'dashboard/product.html')

@login_required(login_url='user-login')
def order(request):
    return render(request, 'dashboard/order.html')