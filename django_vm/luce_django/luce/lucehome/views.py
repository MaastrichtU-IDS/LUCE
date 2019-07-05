from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

from datastore.models import Dataset


def home_page(request):
    head_title = "LUCE"
    # Get first five datasets
    qs = Dataset.objects.all()[:5]
    context = {"head_title": head_title, 
                "dataset_list": qs}
    template = 'home.html'
    return render(request, template, context)

