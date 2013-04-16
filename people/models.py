from django.db import models

# Create your models here.
class Person(models.Model):
    img = models.ImageField(upload_to='images/People/', blank=True)
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    briefBio = models.TextField()
    webaddress = models.URLField(blank=True)
    experience = models.IntegerField()
    phone = models.CharField(max_length=200, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    
    
    def __str__(self):
        return self.firstName + ' ' + self.lastName