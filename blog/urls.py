# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 13:36:32 2017

@author: msdelgosha
"""

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name = 'post_list'),
]