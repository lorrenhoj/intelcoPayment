from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html', {})

def account_info(request):
    return render(request, 'info.html', {})

def method(request):
    return render(request, 'method.html', {})

def gcash(request):
    return render(request, 'gcashpayment.html', {})