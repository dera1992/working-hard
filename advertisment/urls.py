from django.conf.urls import url
from . import views
from django.contrib.auth.views import (
	login,logout,password_reset,password_reset_done,password_reset_confirm,
	password_reset_complete
	)

urlpatterns = [
    url(r'^login/$',login,{'template_name':'advertisment/login.html'}, name='login'),#part10
    url(r'^logout/$',logout,{'template_name':'advertisment/logout.html'}, name= 'logout'), #part14
    url(r'^register/$', views.register,name='register'), #part16
    url(r'^profile/$', views.view_profile,name='view_profile'), #part17
    url(r'^profile/(?P<pk>\d+)/$', views.view_profile,name='view_profile_with_pk'),#part53
    url(r'^profile/edit/$', views.edit_profile,name='edit_profile'), #part18 
    url(r'^change-password/$', views.change_password,name='change_password'), #part20

    url(r'^reset-password/$', password_reset,{'template_name':
    'advertisment/reset_password.html','post_reset_redirect':
    'advertisment:password_reset_done','email_template_name':
    'advertisment/reset_password_email.html'},name='reset_password'),#part21

    url(r'^reset-password/done/$', password_reset_done,{'template_name':'advertisment/reset_password_done.html'},
    name='password_reset_done'),#part21

    url(r'^reset-password/confirm/(?P<uidb64>[0=9A-Za-z]+)-(?P<token>.+)/$',
    password_reset_confirm,{'template_name':'advertisment/reset_password_confirm.html',#part33
    'post_reset_redirect':'advertisment:password_reset_complete'},
    name='password_reset_confirm'),#part21

    url(r'^reset-password/complete/$',password_reset_complete,
    {'template_name':'advertisment/reset_password_complete.html'}#part33
    ,name='password_reset_complete')#part22
]