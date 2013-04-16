'''
Created on 2013-04-11

@author: Ian
'''
from django.conf.urls import patterns, url

from people import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='people')
                       )