from django.http import HttpResponse
# Render allows us to render HTML templates
from django.shortcuts import render
from django.template.loader import get_template

# Python function acts as view
# View receives a request and returns a response
def home_page(request):
	context  = {}
	if request.user.is_authenticated:
		context  = {"title": "Dynamic Title",
				"my_env_var": "Test var content",
				"my_list": [1,2,3,4,5]}
	return render(request, "home.html", context)

def about_page(request):
	return render(request, "about.html", {"title": "About us"})

def contact_page(request):
	return render(request, "contact.html", {"title": "Contact us"})

def example_page(request):
	context 		= {"title": "Example"}
	template_name 	= "hello_world.html"
	template_obj 	= get_template(template_name)
	rendered_item	= template_obj.render(context)
	return HttpResponse(rendered_item)