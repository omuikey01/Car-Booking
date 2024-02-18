from django.db import models

# Create your models here.

class RegisterDealer(models.Model):
    dealer_name = models.CharField(max_length=50)
    dealer_email = models.EmailField(max_length=254)
    dealer_contact = models.CharField(max_length=50)
    dealer_auth = models.CharField(max_length=50)
    dealer_pass = models.CharField(max_length=50)
    dealer_join = models.DateTimeField(auto_now_add=True)

class RegisterUser(models.Model):
    user_name = models.CharField(max_length=50)
    user_email = models.EmailField(max_length=254)
    user_contact = models.CharField(max_length=50)
    user_auth = models.CharField(max_length=50)
    user_pass = models.CharField(max_length=50)
    user_join = models.DateTimeField(auto_now_add=True)
    
    