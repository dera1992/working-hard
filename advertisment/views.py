from django.shortcuts import render,redirect
from advertisment.form import RegistrationForm ,EditProfileForm# part16  
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm 
from django.contrib.auth import update_session_auth_hash #part20
from django.contrib.auth.decorators import login_required #part24 helps to prevent ppl from seeing a page until they log in

# @login_required #part24 helps to prevent ppl from seeing a page until they log in

def register(request):  #part15
	if request.method =='POST':
		
		form = RegistrationForm(request.POST)#part16
		if form.is_valid():
			form.save()
			return redirect(reverse('home:home'))

	else:
		
		form = RegistrationForm()#part16 usercreation form changed to registrationform inform.py

		args = {'form':form}
		return render(request,'advertisment/reg_form.html',args)#part15

# @login_required #part24 helps to prevent ppl from seeing a page until they log in
def view_profile(request, pk=None): #part17
	if pk:  #part53
		user = User.objects.get(pk=pk)
	else:
		user = request.user #part53
	args = {'user':user} # NB we removed the request in the request.user when we added else user
	return render(request,'advertisment/profile.html',args)

# @login_required #part24 helps to prevent ppl from seeing a page until they log in
def edit_profile(request): #part18
	if request.method =='POST':
		form = EditProfileForm(request.POST,instance=request.user) 
		if form.is_valid():
			form.save()
			return redirect(reverse('advertisment:view_profile'))
	else:
		form = EditProfileForm(instance=request.user) #userchangeform was changed to editprofileform in form.py
		args = {'form':form}
		return render(request,'advertisment/edit_profile.html',args)

# @login_required #part24 helps to prevent ppl from seeing a page until they log in
def change_password(request): #part20
	if request.method =='POST':
		form = PasswordChangeForm(data=request.POST,user=request.user)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			return redirect(reverse('advertisment:view_profile'))
		else:
			return redirect(reverse('advertisment:change_password'))

	else:
		
		form = PasswordChangeForm(user=request.user)
		args = {'form':form}
		return render(request,'advertisment/change_password.html',args)
