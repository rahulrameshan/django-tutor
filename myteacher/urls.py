from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from django.contrib import admin
import views

urlpatterns=[
    #url(r'^login/$', auth_views.login),
    #url(r'^sinup/$',views.signup),
    #url(r'^home/$',views.home),
    url(r'^/',views.login),
    url(r'^accounts/',include('registration.backends.simple.urls')),
    url(r'^accounts/profile/',views.profile),
]