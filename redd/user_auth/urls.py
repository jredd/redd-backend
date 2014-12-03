from __future__ import absolute_import

from django.conf.urls import patterns, url

# from .views import dealer_auto_complete, UserDetail
from . import views

urlpatterns = patterns('',
                     #url(r'sist-auth-user-/$', UserRequestList.as_view(), name='job_user'),
                     #url(r'^dealer-auto-complete/$', views.dealer_auto_complete, name='dealer_auto_complete'),
                      url(r'user-detail/(?P<pk>.+)/$', views.UserDetail.as_view(), name='user_detail'),
                      url(r'users-list/$', views.UsersList.as_view(), name='user_list'),
                     #url(r'user-dealer-list/(?P<pk>.+)/$', views.UserDealers.as_view(), name='user_dealer_list'),
                     #url(r'dealer-list/$', DealerList.as_view(), name='dealer_list'),

                     )