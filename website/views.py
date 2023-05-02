from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {})

def account_info(request):
    return render(request, 'info.html', {})

def method(request):
    return render(request, 'method.html', {})
