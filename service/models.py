from django.db import models

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=200)
    intro = models.TextField()
    
    def __str__(self):
        return self.title
    
class Paragraph(models.Model):
    service = models.ForeignKey(Service)
    paragraphPosition = models.IntegerField()
    paragraph = models.TextField()
    
    def __str__(self):
        return str(self.paragraphPosition)
