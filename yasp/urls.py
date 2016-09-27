# coding: utf-8
from __future__ import unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?:(?P<menu_slug>[\w\-]+)/)?(?P<page_slug>[\w\-]+)/?$', views.page, name='page'),
]
