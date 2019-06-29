from django.shortcuts import render, redirect
from django.http import HttpResponse,request, JsonResponse

from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth
from django.contrib.auth.models import User

from bank.models import Member, bc

import hashlib
import hmac
import base64
import json
import requests
# Create your views here.

def bc_set_demand(key,username,rate,_type):          #신청키 이름 이자율 이자타입
        URL = 'http://192.168.150.58:8001/set_demand/'+ key + '-' + username + '-' + rate + '-' + _type
        response = requests.get(URL)
        tx = response.text
        print(response)
        bc(tx = tx,name=username,key=key,rate=rate,_type=_type,org = 'org1').save()
        return tx


def bc_set_bank(key,income,job,position):           #신청키 소득군 직업군
        URL = 'http://192.168.150.58:8001/set_info_bank/'+ key + '-' + income + '-' + job + '-'+ position
        response = requests.get(URL)
        tx = response.text
        
        bc(tx = tx,key=key,income=income,job=job,position = position,org = 'org2').save()

def bc_set_corf(key,income,job,position,_type):           #신청키 소득군 직업군
        URL = 'http://192.168.150.58:8001/set_info_corp/'+ key + '-' + income + '-' + job + '-'+ position
        response = requests.get(URL)
        tx = response.text
        if _type == "1" or _type == "3":    #### 조건변경
            bc(tx = tx,key=key,income=income,job=job,position = position,org = 'org3').save()
        else:#### if변경
            bc(tx = tx,key=key,income=income,job=job,position = position,org = 'org4').save()
        

def bc_get_demand(key):                 #신청키
        URL = 'http://192.168.150.58:8001/get_demand/'+ key
        response = requests.get(URL)
        data = response.json()
        
def bc_get_conf(key):                   #신청키
        URL = 'http://192.168.150.58:8001/get_confirmed/'+ key
        response = requests.get(URL)
        tx = response.text

        bc(tx = tx,key=key).save()



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            request.session['username'] = user.username
            return redirect('/accounts/menu')
        else:
            return render(request, 'accounts/login.html', {'error' : 'check your id and password again'})
    else:
        return render(request, 'accounts/login.html')

def evaluation(request):

    return render(request, 'accounts/evaluation.html', {})

def evaluationReject(request):
    name = request.id
    return render(request, 'accounts/evaluationReject.html', {})

def loading(request):
    user_name = request.user
    customer = Member.objects.get(customer_id = user_name)
    customer.product
    print(customer.product)
    return render(request, 'accounts/loading.html', {'customer_product':customer.product})

def menu(request):
    account_username = request.session['username']
    print(account_username)
    accounts = Member.objects.get(customer_id = account_username)
    print(accounts)

    return render(request, 'accounts/menu.html', {})
    
def loading2(request):
    return render(request, 'accounts/loading2.html', {})

def requestForm(request): 
    return render(request, 'accounts/requestForm.html', {})

def agree(request):
    return render(request, 'accounts/agree.html', {})

def KBscan(request):
    tx_id = bc.objects.all()

    block = []
    for i in tx_id:
        block_list = []
        i.tx
        tx_tx = i.tx.replace('"',"")
        URL = 'http://192.168.150.58:8001/get_block_data/'+tx_tx
    
        response = requests.get(URL)
        result = response.text
        block_data = json.loads(result)
        
        block_list.append(block_data["number"])
        #block_list.append(block_data["previous_hash"])
        block_list.append(block_data["data_hash"])
        
        URL = 'http://192.168.150.58:8001/get_block_timestamp/'+tx_tx
        response = requests.get(URL)
        result = response.text
        
        block_list.append(result)
        
        block_list.append(tx_tx)

        URL = 'http://192.168.150.58:8001/get_tx_status/'+tx_tx
        response = requests.get(URL)
        result = response.text
        if result =='OK':
                result = 'Success'
        #block_list.append(result)
        block_list.append(i.org)

        block.append(block_list)
    
    block2 = []
    for i in tx_id:
        block_list = []
        i.tx
        tx_tx = i.tx.replace('"',"")
        URL = 'http://192.168.150.58:8001/get_block_data/'+tx_tx
    
        response = requests.get(URL)
        result = response.text
        block_data = json.loads(result)
        
        block_list.append(block_data["number"])
        block_list.append(block_data["previous_hash"])
        block_list.append(block_data["data_hash"])
        
        URL = 'http://192.168.150.58:8001/get_block_timestamp/'+tx_tx
        response = requests.get(URL)
        result = response.text
        
        block_list.append(result)
        
        block_list.append(tx_tx)

        URL = 'http://192.168.150.58:8001/get_tx_status/'+tx_tx
        response = requests.get(URL)
        result = response.text
        if result =='OK':
                result = 'Success'
        block_list.append(result)
        block_list.append(i.org)

        block2.append(block_list)
        
    return render(request, 'accounts/KBscan.html', {'block':block,'block2':block2})

def finish(request,tx,cut_rate):
    user_name = request.user
    customer = Member.objects.get(customer_id = user_name)
    print(tx)
    tx = '"' + tx + '"'

    f_bc = bc.objects.get(name=user_name, tx = str(tx) )
    bc_get_conf(f_bc.key)

    return render(request, 'accounts/finish.html', {'cut_rate':cut_rate})

def success(request,r_type):
    user_name = request.user
    print(user_name)    
    print(r_type)
    customer = Member.objects.get(customer_id = user_name)
    customer.reason = r_type
    
    Member.objects.filter(customer_id = user_name).update(reason=r_type)
    user_name = request.user

    tx = bc_set_demand(customer.customer_id,customer.name,customer.int_rate,str(r_type))
    bc_set_bank(customer.customer_id,customer.income,customer.job,customer.position)
    bc_set_corf(customer.customer_id,'2','2','2',str(r_type))

    get_key = bc.objects.get(name=user_name ,tx = tx )
    URL = 'http://192.168.150.58:8001/get_demand/'+get_key.key
    

    response = requests.get(URL)
    response.status_code
    response.text
    print(response.text)
    result = response.text
    a= json.loads(result)
    print(a["cut_rate"])
    tx_tx = tx.replace('"',"")
    return render(request, 'accounts/success.html', {"cut_rate":a["cut_rate"],"pre_rate":customer.int_rate, "tx":tx_tx } )
