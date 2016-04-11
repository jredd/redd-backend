from __future__ import absolute_import

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.DepartmentList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', views.DepartmentDetail.as_view()),
]