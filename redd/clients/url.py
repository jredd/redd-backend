from __future__ import absolute_import

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'$', views.ClientList.as_view()),
]
