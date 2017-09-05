from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    headline = models.CharField(max_length=200)
    content = models.TextField()
    user = models.ForeignKey(User)
    pub_date = models.DateField(auto_now_add=True)
    likes = models.IntegerField(default=0)

    def __str__(self):             
        return self.headline
