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
            return redirect('/user/menu')
        else:
            return render(request, 'user/login.html', {'error' : 'check your id and password again'})
    else:
        return render(request, 'user/login.html')

def evaluation(request):
    return render(request, 'user/evaluation.html', {})

def evaluationReject(request):
    return render(request, 'user/evaluationReject.html', {})

def loading(request):
    return render(request, 'user/loading.html', {})

def menu(request):

    return render(request, 'user/menu.html', {})
    
def loading2(request):
    return render(request, 'user/loading2.html', {})

def success(request):
    return render(request, 'user/success.html', {})

def requestForm(request):
    return render(request, 'user/requestForm.html', {})

def agree(request):
    return render(request, 'user/agree.html', {})
