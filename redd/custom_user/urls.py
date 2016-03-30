from __future__ import absolute_import

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.UsersList.as_view(), name='user_list'),
    url(r'(?P<pk>.+)/$', views.UserDetail.as_view(), name='user_detail'),
]
