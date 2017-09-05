from django.contrib import admin
from advertisment.models import UserProfile #part 11


class UserProfileAdmin(admin.ModelAdmin): #part 38 for customising admin interface to put descriptions to the user
	list_display = ('user','user_info','city','phone','website')

	def user_info(self,obj):
		return obj.description #part 38 for customising admin interface to put descriptions to the user

	def get_queryset(self,request): #part39 admin customise
		queryset = super(UserProfileAdmin,self).get_queryset(request)
		queryset = queryset.order_by('phone','user') # - put in reverse other of arrangement
		return queryset

	user_info.short_description = 'Info' #if u want to rewrite user_info heading in the admin part38

admin.site.register(UserProfile,UserProfileAdmin)#part 11
# admin.site.site_header = 'Adminstration' #part37 for customising admin interface

