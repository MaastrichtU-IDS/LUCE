from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404

# Create your views here.
from .models import BlogPost

def blog_post_detail_page(request, post_id = 1):
	# Handle errors i.e. invalid object id passed into URL
	obj = get_object_or_404(BlogPost, id=post_id)
	template_name 	= 'blog_post_detail.html'
	# Pass in object into context
	context 		= {"object": obj}
	return render(request, template_name, context)