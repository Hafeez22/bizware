from datetime import timezone
from django.db import models

# Create your models here.
#class products(models.Model):
#    pid = models.IntegerField(primary_key = True)
#    pname = models.CharField(max_length = 50)
#    paddress = models.CharField(max_length = 100)
#    size = models.CharField(max_length = 50)
#    pquandity = models.FloatField()
#    pprice = models.FloatField()


class customer(models.Model):
    date = models.DateTimeField()
    cid = models.AutoField(primary_key = True)
    cname = models.CharField(max_length = 50)
    cphone = models.CharField(max_length = 15)
    cmail = models.CharField(max_length = 100)
    caddress = models.CharField(max_length = 200)
    cbalance = models.FloatField()

class suppliers(models.Model):
    date = models.DateTimeField()
    sid = models.AutoField(primary_key=True)
    sname = models.CharField(max_length = 50)
    sphone = models.CharField(max_length = 15)
    smail = models.CharField(max_length = 100)
    saddress = models.CharField(max_length = 100)
    sbalance = models.FloatField()
