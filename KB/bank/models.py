from django.db import models

# Create your models here.

class Member(models.Model):
    
    customer_id=models.CharField(max_length=100, primary_key=True)
    name=models.CharField(max_length=100)
    product=models.CharField(max_length=100)
    product_num=models.CharField(max_length=100)
    account_num=models.CharField(max_length=100)
    screening=models.CharField(max_length=100)
    int_rate=models.CharField(max_length=100)
    grade=models.CharField(max_length=100)
    signed_date=models.DateTimeField()
    reason=models.CharField(max_length=100)
    status=models.CharField(max_length=100)

class Admin(models.Model):

    admin_id=models.CharField(max_length=100,primary_key=True)
    admin_name=models.CharField(max_length=100)
    admin_password=models.CharField(max_length=100)
    admin_mobile=models.CharField(max_length=100)
    admin_email=models.CharField(max_length=100)
    admin_org=models.CharField(max_length=100) # Organization of member
    create_date = models.DateTimeField(auto_now_add=True)
