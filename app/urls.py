from __future__ import unicode_literals

from django.conf.urls import url
from app import views

app_name = 'app'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^accounts/login/$', views.login_user, name='login_user'),

    url(r'^signup/$', views.CreateUser.as_view(), name='sign_up'),

    url(r'^user/(?P<pk>[0-9]+)/$', views.view_user_id, name='profile'),

    url(r'^profile/(?P<user_id>[a-zA_Z0-9]+)/$', views.view_user_name, name='user-profile'),
    url(r'^user/dashboard/$', views.dashboard, name='dashboard'),
    url(r'^accounts/profile/$', views.create_profile, name='profile_make'),
    url(r'^accounts/login/$', views.login_user, name='login_user'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^ride/(?P<user_id>[0-9]+)/$', views.ride, name='ride'),
    url(r'^ride/$', views.ride, name='ride'),



    url(r'^user/(?P<pk>[0-9]+)/update-profile/$', views.EditUser.as_view(), name='user_update'),

    url(r'^logout/$', views.logout_user, name='logout_user'),
    url(r'^login/$', views.do_login, name='login'),



    url(r'^user/(?P<user_id>[0-9]+)/add-ride/$', views.vehicle_create, name='add_ride'),

    url(r'^user/(?P<user_id>[0-9]+)/view-rides/$', views.vehicle_view, name='view_rides'),

    url(r'^user/(?P<user_id>[0-9]+)/delete-ride/(?P<vehicle_id>[0-9]+)/$', views.vehicle_delete, name='delete_ride'),

    url(r'^user/(?P<user_id>[0-9]+)/share-ride/(?P<vehicle_id>[0-9]+)/$', views.vehicle_share, name='share_ride'),

    url(r'^user/(?P<user_id>[0-9]+)/view-shared/$', views.vehicle_shared_view, name='view_shared'),

    url(r'^user/(?P<user_id>[0-9]+)/search/$', views.vehicle_search, name='search_ride'),

    url(r'^user/(?P<user_id>[0-9]+)/request/(?P<ride_id>[0-9]+)', views.request_ride, name='request_ride'),

    url(r'^sharing/(?P<vehicle_share_id>[0-9]+)/view/$', views.view_single_ride, name='view_shared_ride'),

    url(r'^ride/(?P<ride_id>[0-9]+)/view/$', views.view_single_vehicle, name='view_shared_vehicle'),

    url(r'^sharing/(?P<user_id>[0-9]+)/delete/(?P<vehicle_share_id>[0-9]+)/$', views.vehicle_share_delete, name='delete_shared_ride'),

    url(r'^requests/(?P<user_id>[0-9]+)/view$', views.requests_driver_view, name='request_driver_view'),
    url(r'^requests/all$',views.all_ride_requests, name='view_ride_requests'),
    url(r'^request/(?P<request_id>[0-9]+)/approve/$', views.request_approve, name='request_driver_approve'),
    url(r'^request/(?P<request_id>[0-9]+)/deny/$', views.request_deny, name='request_driver_deny'),

    # url(r'^requests/(?P<user_id>[0-9]+)/view$', views.requests_driver_view, name='request_driver_view'),

    url(r'^request/(?P<request_id>[0-9]+)/view/$', views.request_view, name='request_view'),

    url(r'^user/(?P<user_id>[0-9]+)/requests/$', views.requests_user_view, name='requests_user_view'),

    url(r'^request/(?P<request_id>[0-9]+)/delete/$', views.request_delete, name='request_delete'),
    url(r'^user/preferences/$', views.preferences, name='preferences'),

     url(r'^user/preferences/image-update$', views.image_update, name='image_update'),

    url(r'^user/preferences/basic-update$', views.basic_update, name='basic_update'),
    url(r'^user/preferences/user-update$', views.user_update, name='user_update'),
    url(r'^user/preferences/driver-update$', views.driver_update, name='driver_update'),
    url(r'^user/preferences/bio-update$', views.bio_update, name='bio_update'),
    url(r'^user/preferences/app-update$', views.app_update, name='app_update'),
    url(r'^user/preferences/social-update$', views.social_update, name='social_update'),
    url(r'^user/preferences/password-update$', views.password_update, name='password_update'),




]
