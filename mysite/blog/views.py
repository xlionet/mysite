#from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import loader
# Create your views here.

def index( request ):
		
	return HttpResponse("Hello,This is my first site page!");

#def UserLogin( request ):
	
def search( request ):
		print "POST"
		template = loader.get_template('blog/test.html')
		context = {
		}
		return HttpResponse(template.render(context, request))
		
def result( request ):
		print "POST"
		username = request.POST['username']
		password = request.POST['password']
		print username
		print password
		return HttpResponse("i am result!");