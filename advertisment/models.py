from django.db import models
from django.contrib.auth.models import User #part 11
from django.db.models.signals import post_save #part 12

# class UserProfileManage(models.Manager): #part 40
# 	def get_queryset(self):
# 		return  super(UserProfileManage,
# 			self).get_queryset().filter(city='Enugu')
		
class UserProfile(models.Model):#part 11
   user = models.OneToOneField(User)
   description = models.CharField(max_length=100,default='')
   city = models.CharField(max_length=100,default='')
   website= models.URLField(default='')
   phone = models.IntegerField(default=0)#part 11
   image = models.ImageField(upload_to='profile_image',blank = True) #part 36

   # enugu = UserProfileManage() #part 40

   def __str__(self):
      	return self.user.username   #part 35

def create_profile(sender,**kwargs):#part 12 the ebables you to save user profile ones a user is created
	if kwargs['created']:
		user_profile = UserProfile.objects.create(user=kwargs['instance'])
		
post_save.connect(create_profile,sender=User)#part 12