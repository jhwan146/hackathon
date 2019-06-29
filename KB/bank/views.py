from django.shortcuts import render, redirect
from django.http import HttpResponse,request, JsonResponse
from .models import *

from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth
from django.contrib.auth.models import User

import hashlib,hmac,base64,json,requests

# reuse table
total_table = Member.objects.all()
false_table = Member.objects.filter(screening = 'false')
true_table = Member.objects.filter(screening = 'true')


def api():#### 예시
        url = 'https://dev-openapi.kbstar.com:8443/hackathon/getAccountAll'
        data = '{"dataBody":{},"dataHeader":{}}'
        enc_data = data.encode('utf-8')
        key = 'l7xxd3d3817c16c24fa1a64ea99085bab7c5'
        enc_key = key.encode('utf-8')

        hskey = hmac.new(enc_key,enc_data, hashlib.sha256).digest()
        hskey_base64 = base64.b64encode(hskey).decode()

        header = {'Content-Type':'application/json','apikey':key,'hsKey':hskey_base64}
                
        r = requests.post(url, headers = header, data = enc_data)
        r_data = json.loads(r.text)
        return r_data



def main(request):
    try:
        Member.objects.get(name = '나국민')
    except :
        print("나국민 does not exist\n")
        r = api()
        r_product_num = r["dataBody"]["데이터부"][4]["상품번호"]
        r_name = r["dataBody"]["고객명"]
        r_date = r["dataBody"]["데이터부"][4]["상품계약약정년월일"]
        r_account_num =  r["dataBody"]["데이터부"][4]["계좌번호"]
        r_product = r["dataBody"]["데이터부"][4]["상품명"]
        r_id = r["dataBody"]["고객명"]
        Member(customer_id = r_id, name = r_id ,product_num = r_product_num, product = r_product,signed_date = r_date,account_num = r_account_num,income = '3',job='3', position = '3',int_rate = '3.45').save()

    return render(request, 'bank/main.html', {
        'total_num' : len(true_table)+len(false_table), ##전체
        'true_num' : len(true_table), ##승인
        'false_num' : len(false_table) ##거절    
        })

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/bank/main')
        else:
            return render(request, 'bank/login.html', {'error' : 'check your id and password again'})
    else:
        return render(request, 'bank/login.html')

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
    return render(request, 'bank/total.html', { #전체
        'true_table' :  true_table , 'false' : false_table
        })

def scan(request):
    return render(request, 'bank/scan.html', {})

