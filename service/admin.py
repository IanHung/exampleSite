'''
Created on 2013-04-12

@author: Ian
'''
from django.contrib import admin
from service.models import Service, Paragraph

admin.site.register(Service)
admin.site.register(Paragraph)