from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Record
from .forms import RecordForm


def home(request):

    # Check if logging
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            phone_num = form.cleaned_data['phone_num']
            customer_num = form.cleaned_data['customer_num']
            #Check if phone and customer number in database
            record = Record.objects.filter(customer_num=customer_num, phone_num=phone_num).first()
            if record:
                messages.success(request, "Is this your account?")
                return redirect('info', record_id=record.id)
            else:
                messages.success(request, "Account not found")
                return redirect('home')
    else:
        form = RecordForm()
    
    return render(request, 'home.html', {'form':form})


def account_info(request, record_id):
    record = Record.objects.get(id=record_id)
    return render(request, 'info.html', {'record': record})

def logout_user(request):
    logout(request)
    messages.success(request, "You Have Been Logged Out")
    return redirect('home')

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
