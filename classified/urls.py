
from django.conf.urls import url,include
from django.contrib import admin
from classified import views #part14
from django.conf import settings #part36
from django.conf.urls.static import static #part36

urlpatterns = [
    url(r'^$', views.login_redirect,name='login_redirect'), #part14
    url(r'^admin/', admin.site.urls),
    url(r'^advertisment/', include('advertisment.urls', namespace ='advertisment')),
    url(r'^home/', include('home.urls', namespace ='home')),
    url(r'^news/', include('news.urls', namespace ='news')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)#part36
