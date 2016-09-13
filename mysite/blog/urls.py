from django.conf.urls import url
from . import views 

app_name = 'blog'
urlpatterns = [
		url(r'^$', views.index, name="index"),
		url(r'^search/$', views.search, name='search'),
		url(r'^result/$', views.result, name='result'),
]