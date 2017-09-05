from django.db import models #part47
from django.contrib.auth.models import User

class Post(models.Model):
	post = models.CharField(max_length=500)
	user = models.ForeignKey(User)
	created = models.DateTimeField(auto_now_add=True)
	created = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.post

class Friend(models.Model): #remenber ds for ur admin
	users = models.ManyToManyField(User)
	
		
	
