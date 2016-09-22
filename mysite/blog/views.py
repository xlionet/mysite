#from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response,render
from django.template import loader,RequestContext
from django.contrib import auth
from django.views import generic
from django.contrib.auth.models import User
from	models import Article
# Create your views here.

def index( request ):		
	return render(request, 'blog/index.html')

def userLogin( request ):
		return render(request, 'blog/login.html')

def doLogin( request ):
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username=username, password=password)
		m = User.objects.get(username=username)
		if user and user.is_active:
				auth.login(request, user)
				request.session['member_id'] = m.id
				print "login success!"
				return HttpResponseRedirect("/blog/mypage")
		return render_to_response("blog/index.html")
		
def regist( request ):
		print "regist"
		template = loader.get_template('blog/regist.html')
		context = {
		}
		return HttpResponse(template.render(context, request))
		
def doRegist( request ):
		print "doRegist"
		username = request.POST['username']
		usermail = request.POST['email']
		password = request.POST['password']
		user = User.objects.create_user(username,usermail,password)
		user.save()
		return HttpResponse("regist success!")
		
def logout( request ):
		auth.logout(request)
		#del request.session['member_id']
		print "userLogout"
		return HttpResponseRedirect("/blog/index")
		
def	mypage( request ):
		if request.session.get('member_id') is not None:
				template = loader.get_template('blog/mypage.html')
				latest_article_list = Article.objects.order_by('-pub_date')[:5]
				for article in latest_article_list :
						print article.id
				context = {
						'latest_article_list': latest_article_list,
				}
				return HttpResponse(template.render(context, request))
		return HttpResponseRedirect("/blog/index")

def detail(	request, article_id ):
		if request.session.get('member_id') is not None:
				template = loader.get_template('blog/detail.html')
				article = Article.objects.get(pk=article_id)
				context = {
						"article":article,				
				}
				return HttpResponse(template.render(context, request))
		return HttpResponseRedirect("/blog/index")