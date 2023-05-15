from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Record
from .forms import RecordForm


def home(request):
    # Check if logging
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            phone_num = form.cleaned_data['phone_num']
            customer_num = form.cleaned_data['customer_num']

            #Auth
            data = Record.objects.filter(customer_num=customer_num, phone_num=phone_num)
            if data.exists():
                messages.success(request, "Is this your account?")
                return redirect('info')
            else:
                messages.success(request, "Account not found")
                return redirect('home')
    else:
        return render(request, 'home.html', {'form':form})

def logout_user(request):
    logout(request)
    messages.success(request, "You Have Been Logged Out")
    return redirect('home')

def account_info(request):
    form = RecordForm(request.POST)
    form.fields['customer_num'].widget.attrs['disabled'] = True
    form.fields['phone_num'].widget.attrs['disabled'] = True
    return render(request, 'info.html', {'form': form})

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
