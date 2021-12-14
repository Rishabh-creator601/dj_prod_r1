from django.db import models
import os 

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    email = models.EmailField(max_length=122,null=True,blank=True)
    phone_number = models.IntegerField(null=True,blank=True)
    desc  = models.TextField(max_length=500,null=True,blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):

    sweets = "sweets"
    choclates = "choclates"
    junk_food = "Junk Food"

    choices= (
        (sweets,"sweets"),
        (choclates,"choclates"),
        (junk_food,"Junk Food")
    )




    prod_name = models.CharField(max_length=100,null=True,blank=True)
    prod_img = models.ImageField(upload_to="products/",null=True,blank=True)
    price = models.IntegerField()
    prod_desc = models.TextField(max_length=500,null=True,blank=True)
    category = models.CharField(max_length=10,choices=choices,default=sweets)
    id = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.prod_name 

