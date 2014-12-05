from __future__ import absolute_import

from django.contrib.auth.decorators import login_required
from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
                       url(r'asset-list/$', views.AssetList.as_view()),
                      )