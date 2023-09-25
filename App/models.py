from django.db import models

# Create your models here.

class Invoice(models.Model):
    date=models.DateField()
    customer_name=models.CharField(max_length=50)


class InvoiceDetail(models.Model):
    invoice=models.ForeignKey(Invoice,on_delete=models.CASCADE)
    description=models.CharField(max_length=40)
    quantity=models.IntegerField()
    unit_price=models.IntegerField()
    price=models.IntegerField()

    