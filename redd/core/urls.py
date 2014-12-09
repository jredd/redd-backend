from __future__ import absolute_import

from django.conf.urls import patterns, url


from . import views

urlpatterns = patterns('',
                       url(r'projects/$', views.ProjectList.as_view()),
                       url(r'projects/(?P<pk>[0-9]+)/$', views.ProjectDetail.as_view()),
                       url(r'departments/$', views.DepartmentList.as_view()),
                       url(r'departments/(?P<pk>[0-9]+)/$', views.DepartmentDetail.as_view()),
                      )