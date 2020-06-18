from django.conf.urls import url

from . import views

# TODO: pk/up_id
urlpatterns = [
	url(r'^$', views.index, name='index'),
    url(r'^(?P<bunk_id>[0-9]+)/$', views.bunk_detail, name='bunk_detail'),
    url(r'^userprofile/(?P<up_id>[0-9]+)/$', views.user_profile, name='user_profile'),
]
