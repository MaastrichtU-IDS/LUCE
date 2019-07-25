from django.shortcuts import render

from blog.models import BlogPost

from .models import SearchQuery


def search_view(request):
	# Obtain information from URL query & set default value
	query = request.GET.get('q', None)
	# Looks into the request.GET dictionary and looks for
	# key named `q`. If there is none, it will use `None` value.

	context = {"query": query}

	# Obtain user
	user = None
	if request.user.is_authenticated:
		user = request.user

	if query is not None:
		# Store query as entry for log
		SearchQuery.objects.create(user=user, query=query)

		# Obtain matching search results
		blog_list = BlogPost.objects.search(query=query)

		# Add blog_list to context dictionary
		context['blog_list'] = blog_list

	template = 'searches/view.html'
	return render(request, template, context)
