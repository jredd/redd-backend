from __future__ import absolute_import

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'$', views.AssetsList.as_view()),
    url(r'(?P<pk>[0-9]+)/$', views.AssetDetail.as_view()),

    url(r'sub-assets/$', views.SubAssetsList.as_view()),
    url(r'sub-assets/(?P<pk>[0-9]+)/$', views.SubAssetDetail.as_view()),
]