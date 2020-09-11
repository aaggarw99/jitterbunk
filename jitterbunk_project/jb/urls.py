from django.conf.urls import url
from django.urls import include, path
from . import views


urlpatterns = [
    path('api/bunks_list/', views.list_bunks),
    path('api/users_list/', views.list_users),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	url(r'^$', views.index, name='index'),
    url(r'^bunk/(?P<bunk_id>[0-9]+)/$', views.bunk_detail, name='bunk_detail'),
    url(r'^userprofile/(?P<up_id>[0-9]+)/$', views.user_profile, name='user_profile'),
    url(r'^bunked/(?P<user1_id>[0-9]+)/(?P<user2_id>[0-9]+)/$', views.bunk, name='bunked'),
    url(r'^user_feed/(?P<user_id>[0-9]+)/$', views.user_feed, name="user_feed"),
    url(r'^statistics/$', views.bunk_statistics, name="statistics"),
]

app_name = 'jb'