from django.shortcuts import render, redirect
from .models import Dashboard
from django.contrib.auth.decorators import login_required
from django.conf import settings as conf_settings
from django.core.mail import send_mail


# Create your views here.
@login_required
def wallet(request):
    dashboard = Dashboard.objects.all()
    return render(request, 'wallet.html', context={'dashboard':dashboard})
@login_required   
def withdraw(request):
    if request.method == 'POST':
        return redirect('withsuccess')
    return render(request, 'withdraw.html')
@login_required   
def deposit(request):
    if request.method == 'POST':
        return redirect('pay')
    return render(request, 'deposit.html')
@login_required   
def settings(request):
    return render(request, 'settings.html')
@login_required
def topup(request):
    if request.method == 'POST':
        return redirect('pay')
    return render(request, 'topup.html')
   
@login_required   
def btc(request):
    if request.method == 'POST':
        return redirect('success')
    return render(request, 'btc.html')
    
@login_required   
def usdt(request):
    if request.method == 'POST':
        return redirect('success')
    return render(request, 'usdt.html')
    
    