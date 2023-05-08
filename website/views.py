from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import time


def home(request):
    return render(request, 'home.html', {})

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
