'''
Created on 2013-04-12

@author: Ian
'''
from django.contrib import admin
from price.models import SimplePrice, PackagePrice

admin.site.register(SimplePrice)
admin.site.register(PackagePrice)