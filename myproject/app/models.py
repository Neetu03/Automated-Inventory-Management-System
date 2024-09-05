from django.db import models

# Create your models here.



class Products(models.Model):
    CATEGORY_CHOICES = (
    ('Electronics', 'Option 1'),
    ('Clothing', 'Option 2'),
    ('Furniture', 'Option 3'),)
    product_name=models.CharField(max_length=100)
    Quantity=models.IntegerField()
    Price=models.IntegerField()
    Category=models.CharField(max_length=50,choices=CATEGORY_CHOICES)
    

class transactions(models.Model):
    TRANSACTION_TYPES = (
        ('IN', 'Incoming stock'),
        ('OUT', 'Outgoing stock'),
    )
    TransactionType=models.CharField(max_length=3,choices=TRANSACTION_TYPES)
    CATEGORY_CHOICES = (
    ('Electronics', 'Option 1'),
    ('Clothing', 'Option 2'),
    ('Furniture', 'Option 3'),)
    ProductID = models.ForeignKey(Products, on_delete=models.CASCADE)
    Quantity=models.IntegerField()
    TransactionDate=models.DateField(auto_now=True)
    Category=models.CharField(max_length=50,choices=CATEGORY_CHOICES)