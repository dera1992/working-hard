from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.template.context import RequestContext
from django.db.models import Q

from news.forms import ArticleForm
from news.models import Article

def create_articles(request):
    if request.POST:
    	form = ArticleForm(request.POST)
    	if form.is_valid():
	    		post = form.save(commit=False)
	    		post.user = request.user
	    		post.save()

	    		# text = form.cleaned_data['headline','content']
	    		messages.add_message(request,messages.SUCCESS,'Your Articles was added')
	    		form = ArticleForm()
	    		return redirect('home:home')
    	
    else:
    	form = ArticleForm()

    	args = {'form':form}
    	return render(request, 'news/create_articles.html', args)
    

# def  get_articles(request): #DIS WAS MOVE TO THE VIEW OF home dat is where it is
# 	form = ArticleForm()
# 	articles = Article.objects.all().order_by('-pub_date')
# 	users = User.objects.exclude(id=request.user.id) 

# 	return render(request,'home/home.html',{'articles':articles,'users':users})

def view_article(request, article_id=1):
	article = Article.objects.get(id = article_id)
	return render(request,'news/article.html',{'article':article})

def like_feed(request,article_id=0):
	if article_id:
		a = Article.objects.get(id=article_id)
		count = a.likes
		count += 1
		a.likes = count
		a.save()

	return redirect('/news/get/%s' % article_id)

def  search_titles(request):
	if request.method == 'POST':
		search_text = request.POSTS['search_text']
	else:
		search_text = ''

	articles = Article.objects.filter(headline__contains=search_text)
	return render('news/ajax_search.html',{'articles':articles})


# def search_titles( request ):

#     if request.is_ajax():
#         q = request.GET.get( 'q' )
#         if q is not None:            
#             results = Article.objects.filter( 
#                 Q( headline__contains = q ) )
                
#     return render('news/ajax_search.html' , { 'results': results, }, 
#                   context_instance = RequestContext( request ) )

	