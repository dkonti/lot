from django.shortcuts import render, redirect
from .models import Hashrate
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    hashrate = Hashrate.objects.all()
    if request.method == 'POST':
        name = request.POST.get('contact-name')
        email = request.POST.get('contact-email')
        message = request.POST.get('contact-message')
        main = str(message)
        send_mail('Contact Form from ' + str(name), main, email, ['petsmartcharities@mail.ru'], fail_silently=False)
    return render(request, 'home.html', context={'hashrate':hashrate})

@login_required     
def signals(request):
    return render(request, 'signal.html')
       
def success(request):
    return render(request, 'success.html')
    
def rsuccess(request):
    return render(request, 'rsuccess.html')
    
def invest(request):
    if request.method == 'POST':
        return redirect('pay')
    return render(request, 'invest.html')
@login_required    
def psignal(request):
    if request.method == 'POST':
        return redirect('pay')
    return render(request, 'psignal.html')
    
def buycrypto(request):
    return render(request, 'buycrypto.html')
    
def about(request):
    return render(request, 'about.html')
@login_required    
def pay(request):
    if request.method == 'POST':
        return redirect('success')
    return render(request, 'pay.html')
@login_required    
def accessories(request):
    return render(request, 'accessories.html')
@login_required    
def baccessories(request):
    if request.method == 'POST':
        return redirect('pay')
    return render(request, 'baccessories.html')