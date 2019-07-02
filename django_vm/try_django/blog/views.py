from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404

# Create your views here.
from .models import BlogPost

# Import forms
from .forms import BlogPostModelForm

# CRUD

# GET -> Retrieve / Read
# POST -> Create / Update / Delete

# Create Retrieve Update Delete

# We create a view for each of these functionalities
def blog_post_list_view(request):
	# list out objects
	# could be search
	qs = BlogPost.objects.all() # queryset -> list of python objects
	template 	= 'blog/list.html'
	context 	= {'object_list': qs}
	return render(request, template, context)

def blog_post_create_view(request):
	# create objects
	# how? use a form
	form = BlogPostModelForm(request.POST or None)
	if form.is_valid():
		form.save()
		# To change the form content before saving:
		# obj = form.save(commit=False)
		# obj.title = form.cleaned_data.get("title") + "_My_Suffix"
		# obj.save()
		form = BlogPostModelForm()
	template 	= 'blog/form.html'
	context 	= {'form': form}	
	return render(request, template, context)

# Retireve view or detail view
def blog_post_detail_view(request, slug):
	# 1 object -> detail view
	template 	= 'blog/detail.html'
	obj 		= get_object_or_404(BlogPost, slug=slug)
	context 	= {'object': obj}
	return render(request, template, context)

def blog_post_update_view(request, slug):
	template 	= 'blog/update.html'
	obj 		= get_object_or_404(BlogPost, slug=slug)
	context 	= {'object': obj, 
					'form': None}
	return render(request, template, context)


def blog_post_delete_view(request, slug):
	template 	= 'blog/delete.html'
	obj 		= get_object_or_404(BlogPost, slug=slug)
	context 	= {'object': obj}
	return render(request, template, context)
