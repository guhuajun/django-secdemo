# -*- coding: utf-8 -*-
# pylint: disable=

"""
Definition of urls for web.
"""

from django.urls import re_path

from frontend import views

urlpatterns = [
    re_path('^', views.IndexView.as_view(), name='index')
]
