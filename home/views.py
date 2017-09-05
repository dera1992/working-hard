from django.views.generic import TemplateView #part 43
from django.shortcuts import render,redirect
from django.contrib.auth.models import User #part 52

from home.forms import HomeForm
from  home.models import Post
from news.models import Article
from django.contrib import messages
from django.conf import settings

def home(request):
	if request.POST:
		form = HomeForm(request.POST)
		if form.is_valid():
		    	post = form.save(commit=False)
		    	post.user = request.user
		    	post.save()

		    	text = form.cleaned_data['post']
		    	messages.success(request,'Your post was added')
		    	form = HomeForm()
	    		return redirect('home:home')
	articles = Article.objects.all().order_by('-pub_date')
	form = HomeForm()
	posts = Post.objects.all().order_by('-created')
	users = User.objects.exclude(id=request.user.id) 
	return render(request,'home/home.html',{'form':form,'posts':posts,'users':users,'articles':articles})
# class HomeView(TemplateView):
# 	template_name = 'home/home.html'


# 	def  get(self,request):
# 		form = HomeForm()
# 		# posts = Post.objects.all().order_by('-created')
# 		# users = User.objects.exclude(id=request.user.id) #part 52

# 		args = {'forms': form}
# 		return render(request,self.template_name,args)

	
# 	# def post(self,request): #part46
# 	#     form = HomeForm(request.POST)
# 	#     if form.is_valid():
# 	#     	post = form.save(commit=False)
# 	#     	post.user = request.user
# 	#     	post.save()

# 	#     	text = form.cleaned_data['post']
# 	#     	form = HomeForm()
# 	#     	return redirect('home.home')

# 	#     args = {'form':form,'text':text}
# 	#     return render(request,self.template_name,args)

def  delete_comment(request,post_id):
	c = Post.objects.get(id=post_id)

	# article_id = c.article_id

	c.delete()

	messages.add_message(request,
		settings.DELETE_MESSAGE,
		'Your comment was deleted')

	return redirect(reverse('home:home'))






	
		
