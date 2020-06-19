from django.conf.urls import url

from . import views

# TODO: pk/up_id
urlpatterns = [
	url(r'^$', views.index, name='index'),
    url(r'^bunk/(?P<bunk_id>[0-9]+)/$', views.bunk_detail, name='bunk_detail'),
    url(r'^userprofile/(?P<up_id>[0-9]+)/$', views.user_profile, name='user_profile'),
    url(r'^bunked/(?P<user1_id>[0-9]+)/(?P<user2_id>[0-9]+)/$', views.bunk, name='bunked'),
    url(r'^user_feed/(?P<user_id>[0-9]+)/$', views.user_feed, name="user_feed"),
]
