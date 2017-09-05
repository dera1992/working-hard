#for search url
url(r'^search/', views.search_titles, name ='search'),

#for d views
def  search_titles(request):
	if request.method == 'POST':
		search_text = request.POST['search_text']
	else:
		search_text = ''

	articles = Article.objects.filter(headline__contains=search_text)
	return render(request,'news/ajax_search.html',{'articles':articles})

#ajax_search.html
{% if articles.count > 0 %}

{% for article in articles %}
        <li><a href="{% url 'news:view_article' article.id %}">{{article.headline}}</a></li>
{% endfor %}

{% else %}

<li> None to show! </li>

{% endif %}


#in the home html

<h3> Search </h3>
{% csrf_token %}
<input type = 'text' id = 'search' name = 'search' />

<ul id = 'search-results'>

</ul>

#ajax.js
$(function() {

	$('#search').keyup(function() {

		$.ajax({
			type: "POST",
			url : 'news:search',
			data: {
			     'search_text' : $('#search').val(),
			     'csrfmiddlewaretoken' : $("input [name=csrfmiddlewaretoken]").val()
			},
			success: searchSuccess,
			dataType: 'html'
			});
		});
	});

function searchSuccess(data, textStatus,jqXHR)
{
	$('#search-results') . html(data);
}


#this is for messaging after deleting a comment. remenber to save the changes at setting

#at the url

url(r'^delete_comment/(?P<post_id>d+)/$', views.delete_comment, name='delete_comment')


#in the views

from django.contrib import messages #put dis both in news and home views

def  delete_comment(request,post_id):
	c = Post.objects.get(id=post_id)

	# article_id = c.article_id

	c.delete()

	messages.add_message(request,
		settings.DELETE_MESSAGE,
		'Your comment was deleted')

	return redirect('home:home')


#NOTIFICATION
#CREATE AN APP FOR IT called notification

register it in setting.py

#model.py
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signal import post_save
from django.dispatch import receiver


class Notification(models.Model):
 	title = models.CharField(max_lenght=256)
 	message = models.TextField()
 	viewed = models.BooleanField(default=False)
 	user = models.ForeignKey(User)

@receiver(post_save, sender=User)
def create_welcome_message(sender,**kwargs):
	if kwargs.get('created',False):
		Notification.objects.create(user=kwargs.get('instance'),
			title='Welcome to our Django site!',
			message='Thanks for signing up!')

#url
from django.conf.urls import url

from notification import views

urlpatterns = [
    url(r'^show/(?P<article_id>\d+)/$', views.show,name='show'),
    url(r'^delete_not/(?P<article_id>\d+)/$',views.delete_note,name='delete_not'),
]

#views
from django.shortcuts import render,redirect
from models import Notification

def show(request,notification_id):
	n = Notification.objects.get(id=notification_id)
	return render('notification/show.html',{'notification':n})

def delete_note(request,notification_id):
	n = Notification.objects.get(id=notification_id)
	n.viewed = True
	n.save()

	return redirect('home:home')

#show.html
{% extends 'base.html' %} 

{% block body %}
<div class="container">
    <h1>{{notification.title}}</h1>
    <p>{{notification.message}}</p>
    <p><a href="{% url 'notification:delete_note' notification.id %}">Mark as read</a></p>
    <br>
</div>
 
{% endblock %}

#dis will be in the home .html

{% if notifications.count > 0 %}
    <h3> Notification </h3>
	{% for n in notifications %}
       <p><a href="{% url 'notification:show' n.id %}">{{n.title}}</a></p>
	{% endfor %}
{% endif %}

#go to home.view and add notification model

from notification.models import Notification

n = Notification.objects.filter(user=request.user, viewed=False)

'notification':n


	
