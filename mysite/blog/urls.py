from django.conf.urls import url
from . import views 

app_name = 'blog'
urlpatterns = [
		url(r'^index/$', views.index, name="index"),
		url(r'^regist/$', views.regist, name='regist'),
		url(r'^doRegist/$', views.doRegist, name='doRegist'),
		url(r'^login/$', views.userLogin, name='userlogin'),
		url(r'^doLogin/$', views.doLogin, name='doLogin'),
		url(r'^logout/$', views.logout, name='logout'),
		url(r'^mypage/$', views.mypage, name='mypage'),
		url(r'^(?P<article_id>[0-9]+)/$', views.detail, name='detail'),
]