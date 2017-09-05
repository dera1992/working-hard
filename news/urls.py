from django.conf.urls import url

from news import views

urlpatterns = [
    url(r'^create_articles/$', views.create_articles , name='create_articles'),
    url(r'^get/(?P<article_id>\d+)/$', views.view_article,name='view_article'),
    url(r'^likes/(?P<article_id>\d+)/$',views.like_feed,name='like'),
    url(r'^search/', views.search_titles, name ='search'),
]