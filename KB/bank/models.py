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