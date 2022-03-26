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
        invest = request.POST.get('invest')
        amount = request.POST.get('asset')
        subject = 'Withdraw'
        send_to = ['libertexonlinetrading@yahoo.com',]
        current_user = request.user
        message = 'I want to make a ' + str(invest) + ' withdrawal of ' + str(amount) + ' from ' + str(current_user)
        
        send_mail(subject, message, conf_settings.EMAIL_HOST_USER, send_to)
        
        return redirect('pay')
    return render(request, 'withdraw.html')
@login_required   
def deposit(request):

    if request.method == 'POST':
        invest = request.POST.get('invest')
        amount = request.POST.get('asset')
        subject = 'Deposit'
        send_to = ['libertexonlinetrading@yahoo.com',]
        current_user = request.user
        message = 'I want to make a ' + str(invest) + ' deposit of ' + str(amount) + ' from ' + str(current_user)
        
        send_mail(subject, message, conf_settings.EMAIL_HOST_USER, send_to)
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
    return render(request, 'btc.html')
    
@login_required   
def usdt(request):
    return render(request, 'usdt.html')
    
    