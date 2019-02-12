# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 17:16:15 2019

@author: 10536
"""

from django.conf.urls import url
from rango import views



urlpatterns = [
        url(r'^$',views.index,name='index'),
        url(r'^about/',views.about,name='about'),
        url(r'^add_category/$', views.add_category, name='add_category'),
        url(r'^category/(?P<category_name_slug>[\w\-]+)/$',
            views.show_category, name='show_category'),
] 
