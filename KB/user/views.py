from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, 'user/login.html', {})

def evaluation(request):
    return render(request, 'user/evaluation.html', {})

def evaluationReject(request):
    return render(request, 'user/evaluationReject.html', {})

def loading(request):
    return render(request, 'user/loading.html', {})

def menu(request):
    return render(request, 'user/menu.html', {})
    

