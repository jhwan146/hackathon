from django.shortcuts import render
from django.http import HttpResponse,request, JsonResponse
from .models import *

# reuse table
total_table = Member.objects.all()
false_table = Member.objects.filter(screening = 'false')
true_table = Member.objects.filter(screening = 'true')

def main(request):

    return render(request, 'bank/main.html', {
        'total_num' : len(total_table), ##전체
        'true_num' : len(true_table), ##승인
        'false_num' : len(false_table) ##거절 
        })

def index(request):
    #..
    return render(request, 'bank/index.html', {})

def passed(request):

    return render(request, 'bank/passed.html', {
        'true_table' : true_table
    })

def rejected(request):
    return render(request, 'bank/rejected.html', { #반려
        'false_table' : false_table
        })

def total(request):
    return render(request, 'bank/total.html', {#전체
        'total_table' :  total_table
        })
