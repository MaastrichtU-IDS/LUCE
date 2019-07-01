from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404

# Create your views here.
from .models import BlogPost

# GET -> 1 object
# filter -> [] objects (QuerySet)

def blog_post_detail_page(request, slug):
	template 	= 'blog_post_detail.html'
	# Pass in object into context
	obj 		= get_object_or_404(BlogPost, slug=slug)
	context 	= {"object": obj}
	return render(request, template, context)