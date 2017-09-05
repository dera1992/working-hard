from django import forms
from news.models import Article

class ArticleForm(forms.ModelForm):
	# content = forms.TextField(required = True)
	
	class Meta:
		model = Article
		fields = ('headline','content')
			
