'''
Created on 2013-04-12

@author: Ian
'''
from django.contrib import admin
from contactList.models import Location, Email

admin.site.register(Location)
admin.site.register(Email)