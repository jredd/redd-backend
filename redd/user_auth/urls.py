from __future__ import absolute_import

from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
                      url(r'user-detail/(?P<pk>.+)/$', views.UserDetail.as_view(), name='user_detail'),
                      url(r'users-list/$', views.UsersList.as_view(), name='user_list'),
                     )