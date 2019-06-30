from django.http import HttpResponse
# Render allows us to render HTML templates
from django.shortcuts import render
from django.template.loader import get_template

# Python function acts as view
# View receives a request and returns a response
def home_page(request):
	my_title = "Dynamic Title"
	my_content = "Test content"
	context  = {"title": my_title,
				"content": my_content}
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