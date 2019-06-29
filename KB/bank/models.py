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
    income=models.CharField(max_length=100)
    job=models.CharField(max_length=100)
    position=models.CharField(max_length=100)
    signed_date=models.CharField(max_length=100)
    reason=models.CharField(max_length=100)
    status=models.CharField(max_length=100)

class bc(models.Model):
    tx=models.CharField(max_length=100, primary_key=True)
    key=models.CharField(max_length=100)
    org=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    rate=models.CharField(max_length=100)
    _type=models.CharField(max_length=100)
    income=models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    position = models.CharField(max_length=100)