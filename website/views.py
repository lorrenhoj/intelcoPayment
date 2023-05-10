from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpResponseRedirect


def home(request):
    # Check if logging
    if request.method == 'POST':
        phone = request.POST['phone']
        account = request.POST['account']
        # Auth
        user = authenticate(request, phone=phone, account=account)
        if user is not None:
            login(request, user)
            messages.success(request, "Is this your account?")
            return redirect('home')
        else:
            messages.success(request, "Account not found")
            return redirect('home')
    else:
        return render(request, 'home.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, "You Have Been Logged Out")
    return redirect('home')

def account_info(request):
    return render(request, 'info.html', {})


def payment_method(request):
    if request.method == 'POST':
        payment_method = request.POST.get('payment_method')
        if payment_method == 'credit':
            return render(request, 'credit.html')
        elif payment_method == 'gcash':
            return render(request, 'gcash.html')
    return render(request, 'payment.html')

def success(request):
    return render(request, 'success.html')
