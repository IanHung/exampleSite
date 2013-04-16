from django.db import models

# Create your models here.
class SimplePrice(models.Model):
    title = models.CharField(max_length=200)
    price = models.IntegerField()
        
    def __str__(self):
        return self.title
    
class PackagePrice(models.Model):
    title = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField()
    service = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title
