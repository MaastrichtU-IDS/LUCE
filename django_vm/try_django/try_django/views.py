from django.http import HttpResponse
# Render allows us to render HTML templates
from django.shortcuts import render

# Python function acts as view
# View receives a request and returns a response
def home_page(request):
	return render(request, "hello_world.html")

def about_page(request):
	return HttpResponse("<h1>About Page</h1>")

def contact_page(request):
	return HttpResponse("<h1>Contact Page</h1>")