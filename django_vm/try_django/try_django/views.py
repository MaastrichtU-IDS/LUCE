from django.http import HttpResponse
# Render allows us to render HTML templates
from django.shortcuts import render

# Python function acts as view
# View receives a request and returns a response
def home_page(request):
	my_title = "Dynamic Title"
	# doc = "<h1>{title}</h1>".format(title=my_title)
	# django_rendered_doc = "<h1>{{title}}</h1>".format(title=my_title)
	return render(request, "hello_world.html", {"title": my_title})

def about_page(request):
	return render(request, "about.html", {"title": "About us"})

def contact_page(request):
	return render(request, "contact.html", {"title": "Contact us"})