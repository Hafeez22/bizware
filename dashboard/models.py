from django.db import models

# Create your models here.

class size(models.Model):
    sid = models.AutoField(primary_key=True)
    size = models.CharField(max_length = 50)
   


class products(models.Model):
    choices = [
        ('Not coated','Not coated'),
        ('Coated','Coated'),
        ('Silver coated','Silver coated'),
    ]
    date = models.DateTimeField()
    pid = models.AutoField(primary_key= True)
    pname = models.CharField(max_length = 100)
    psize = models.ForeignKey(size, on_delete = models.CASCADE)
    pzinc = models.CharField(choices=choices, max_length = 50)
    pprice = models.DecimalField(max_digits = 10, decimal_places = 2)
    psellingprice = models.DecimalField(max_digits = 10, decimal_places = 2)