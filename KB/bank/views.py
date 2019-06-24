from django.shortcuts import render
from django.http import HttpResponse,request, JsonResponse
from .models import *

# Create your views here.

def main(request):
    return render(request, 'bank/main.html', {})

def index(request):
    return render(request, 'bank/index.html', {})

def passed(request):
    return render(request, 'bank/passed.html', {})

def rejected(request):
    return render(request, 'bank/rejected.html', {})

def total(request):

    total_table = Member.objects.all()

    return render(request, 'bank/total.html', {'total_table': total_table})
