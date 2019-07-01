from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404

# Create your views here.
from .models import BlogPost

# GET -> 1 object
# filter -> [] objects (QuerySet)

def blog_post_detail_page(request, slug):
	# Print information to server terminal
	print("DJANGO says", 
		request.method, 
		request.path,
		request.user)

	template 	= 'blog_post_detail.html'
	# Pass in object into context
	obj 		= get_object_or_404(BlogPost, slug=slug)
	context 	= {"object": obj}
	return render(request, template, context)

# CRUD

# GET -> Retrieve / Read
# POST -> Create / Update / Delete

# Create Retrieve Update Delete

# We create a view for each of these functionalities
def blog_post_list_view(request):
	# list out objects
	# could be search
	template 	= 'blog_post_list.html'
	context 	= {'form': None}
	return render(request, template, context)

def blog_post_create_view(request):
	# create objects
	# how? use a form
	template 	= 'blog_post_create.html'
	context 	= {'object_list': []}
	return render(request, template, context)

# Retireve view or detail view
def blog_post_detail_view(request):
	# 1 object -> detail view
	template 	= 'blog_post_detail.html'
	obj 		= get_object_or_404(BlogPost, slug=slug)
	context 	= {'object': obj}
	return render(request, template, context)

def blog_post_update_view(request):
	template 	= 'blog_post_update.html'
	obj 		= get_object_or_404(BlogPost, slug=slug)
	context 	= {'object': obj, 
					'form': None}
	return render(request, template, context)


def blog_post_delete_view(request):
	template 	= 'blog_post_delete.html'
	obj 		= get_object_or_404(BlogPost, slug=slug)
	context 	= {'object': obj}
	return render(request, template, context)
