from django.conf.urls import url, include  #part 42
from home.views import home,delete_comment  #part43



urlpatterns = [
   url(r'^$', home, name ='home'), #part 42
   url(r'^delete_comment/(?P<post_id>.*)/$', delete_comment, name='delete_comment'),
]


