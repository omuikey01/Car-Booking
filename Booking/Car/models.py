from django.db import models

# Create your models here.

class RegisterDealer(models.Model):
    dealerfullname = models.CharField(max_length=50)
    dealemail = models.EmailField(max_length=254)
    dealcontact = models.CharField(max_length=50)
    dealerauth = models.CharField(max_length=50)
    dealerpass = models.CharField(max_length=50)
    
    