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

# def dev_view(request):
#     head_title = "LUCE"
#     # Get first five datasets
#     qs = Dataset.objects.all()[:5]
#     context = {"head_title": head_title, 
#                 "dataset_list": qs}
#     template = 'dev.html'
#     return render(request, template, context)

def dev_view(request):

    if(request.GET.get('mybtn_2')):
        print("Second button was pressed")

    if(request.GET.get('mybtn_3')):
        print("Third button was pressed")

    if(request.GET.get('mybtn_4')):
        print("Forth button was pressed")        

    if(request.GET.get('mybtn')):
        print( int(request.GET.get('mytextbox')) ) # or any other function

    context = {}
    template = 'dev.html'
    return render(request, template, context)
    