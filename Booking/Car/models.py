from django.db import models

# Create your models here.

class RegisterDealer(models.Model):
    dealer_name = models.CharField(max_length=50)
    dealer_email = models.EmailField(max_length=254)
    dealer_contact = models.CharField(max_length=50)
    dealer_auth = models.CharField(max_length=50)
    dealer_pass = models.CharField(max_length=50)
    dealer_join = models.DateTimeField(auto_now_add=True)
    def __str__(om):
        return om.dealer_name


class RegisterUser(models.Model):
    user_name = models.CharField(max_length=50)
    user_email = models.EmailField(max_length=254)
    user_contact = models.CharField(max_length=50)
    user_auth = models.CharField(max_length=50)
    user_pass = models.CharField(max_length=50)
    user_join = models.DateTimeField(auto_now_add=True)
    
class Images(models.Model):
    image = models.ImageField(upload_to='images') 

class ProductAdd(models.Model):
    dealer_id = models.IntegerField()
    # dealer_id = models.ManyToManyField(RegisterDealer)
    car_name = models.CharField(max_length=100)
    car_color = models.CharField(max_length=100)
    amt_per_km = models.IntegerField()
    discount_per = models.IntegerField(blank=True)
    image1 = models.ImageField(upload_to='images', blank=True)
    image2 = models.ImageField(upload_to='images', blank=True)
    image3 = models.ImageField(upload_to='images', blank=True)
    image4 = models.ImageField(upload_to='images', blank=True)
    image5 = models.ImageField(upload_to='images', blank=True)
