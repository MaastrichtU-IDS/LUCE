from django.http import HttpResponse

# Python function acts as view
# View receives a request and returns a response
def home_page(request):
	# function body creates content of view
	return HttpResponse("<h1>Hello World</h1>")