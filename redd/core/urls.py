from __future__ import absolute_import

from django.conf.urls import patterns, url


from . import views

urlpatterns = patterns('',
                       url(r'project-list/$', views.ProjectList.as_view()),
                       url(r'project-detail/(?P<pk>[0-9]+)/$', views.ProjectDetail.as_view()),
                       url(r'department-list/$', views.DepartmentList.as_view()),
                      )