from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=200)
    streetAddress = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    province = models.CharField(max_length=200)
    country = models.CharField(max_length=200, blank=True)
    postalCode= models.CharField(max_length=200)
    phone = models.CharField(max_length=200, blank =True)
    map = models.ImageField(upload_to='images/contactList/', blank=True)
    priority = models.IntegerField(default=2)
    
    def __str__(self):
        return self.name
    
class Email(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return self.name