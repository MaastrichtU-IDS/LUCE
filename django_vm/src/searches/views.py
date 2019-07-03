from django.shortcuts import render

from .models import SearchQuery


def search_view(request):
	# Obtain information from URL query & set default value
	query = request.GET.get('q', None)
	# Looks into the request.GET dictionary and looks for
	# key named `q`. If there is none, it will use `None` value.

	# Obtain user
	user = None
	if request.user.is_authenticated:
		user = request.user

	# Store query as entry for log
	SearchQuery.objects.create(user=user, query=query)

	template = 'searches/view.html'
	context = {"query": query}
	return render(request, template, context)
