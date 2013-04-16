'''
Created on 2013-04-12

@author: Ian
'''
from django.conf.urls import patterns, url

from service import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='service')
                       )