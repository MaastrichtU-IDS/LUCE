from django.shortcuts import render
from django.shortcuts import get_object_or_404

# Create your views here.
from .models import Dataset

def view_dataset_page(request, dataset_id = 1):
	# Handle errors i.e. invalid object id passed into URL
	dataset_object 	= get_object_or_404(Dataset, id=dataset_id)
	template 		= 'view_dataset.html'
	# Pass dataset object into context for website
	# This way the object is available as an
	# 'environment variable' to use in the page
	context 		= {"dataset": dataset_object}
	return render(request, template, context)