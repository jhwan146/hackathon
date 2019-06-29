from django.shortcuts import render, redirect
from django.http import HttpResponse,request, JsonResponse
from .models import * 

from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.

def login(request):
    if request.method == 'POST':
        
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/accounts/menu')
        else:
            return render(request, 'accounts/login.html', {'error' : 'check your id and password again'})
    else:
        return render(request, 'accounts/login.html')

def evaluation(request):
    return render(request, 'accounts/evaluation.html', {})

def evaluationReject(request):
    return render(request, 'accounts/evaluationReject.html', {})

def loading(request):
    return render(request, 'accounts/loading.html', {})

def menu(request, accounts_id):
    accounts = get_object_or_404(User, id=accounts_id)
    
    if accounts.user != request.user:
        return redirect('accounts/login.html')
    
    return render(request, 'accounts/menu.html', {})
    
def loading2(request):
    return render(request, 'accounts/loading2.html', {})

def success(request):
    return render(request, 'accounts/success.html', {})

def requestForm(request):
    return render(request, 'accounts/requestForm.html', {})

def agree(request):
    return render(request, 'accounts/agree.html', {})
