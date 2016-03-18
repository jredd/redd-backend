from __future__ import absolute_import

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'$', views.ProjectList.as_view())
    # url(r'projects/(?P<pk>[0-9]+)/$', )
]
