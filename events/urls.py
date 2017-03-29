from django.conf.urls import url
from django.contrib import admin
# from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^$', views.list),
    url(r'^create/$', views.create),
    url(r'^detail/$', views.detail),
    url(r'^register/$', views.register),
    url(r'^user/$', views.userprofile),
    url(r'^login/$', views.login),

    #url()
    # url(r'^$', auth_views.login),
	# url(r'^logout/$', views.logout_page),




]
