'''
Created on 2013-04-12

@author: Ian
'''
from django.contrib import admin
from people.models import Person

admin.site.register(Person)