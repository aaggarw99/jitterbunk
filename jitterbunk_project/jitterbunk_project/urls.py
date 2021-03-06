"""jitterbunk_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
# from django.contrib.auth import views as auth 
# from user import views as user_view 

urlpatterns = [
    url(r'^', include('jb.urls', namespace='jb')),
    url(r'^admin/', admin.site.urls),
]

# path('', include('user.urls')), 
# path('login/', user_view.Login, name ='login'), 
# path('logout/', auth.LogoutView.as_view(template_name ='user / index.html'), name ='logout'), 
# path('register/', user_view.register, name ='register'), 

#Add Django site authentication urls (for login, logout, password management)

urlpatterns += [
    url('accounts/', include('django.contrib.auth.urls')),
]