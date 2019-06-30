from django.http import HttpResponse

# Python function acts as view
# View receives a request and returns a response
def home_page(request):
	# function body creates content of view
	return HttpResponse("<h1>Hello World</h1>")

def about_page(request):
	return HttpResponse("<h1>About Page</h1>")

def contact_page(request):
	return HttpResponse("<h1>Contact Page</h1>")