#from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response,render
from django.template import loader,RequestContext
from django.contrib import auth
from django.views import generic
from django.contrib.auth.models import User
# Create your views here.

def index( request ):
		
	return render(request, 'blog/index.html')

def userLogin( request ):
		return render(request, 'blog/login.html')

def doLogin( request ):
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username=username, password=password)
		if user and user.is_active:
				auth.login(request, user)
				print "login success!"
				return HttpResponseRedirect("/blog/index")
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
		print "userLogout"
		return HttpResponseRedirect("/blog/index")