from django.shortcuts import render, get_object_or_404


from datastore.models import Dataset
from datastore.forms import DatasetModelForm


def upload_view(request):
    form = DatasetModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        # Obtain data from form
        obj = form.save(commit=False)
        # Add user attribute
        obj.user = request.user
        # Save to database
        obj.save()
        # Refresh to blank form 
        # (!!!) Maybe display "Success" message and go to detail view for dataset
        form = DatasetModelForm()
    context = {
            'form': form
                }
    template = 'data/upload.html'
    return render(request, template, context)


def browse_view(request):
    head_title = "LUCE"
    # Get first five datasets
    qs = Dataset.objects.all()[:5]
    context = {"head_title": head_title, 
                "dataset_list": qs}
    template = 'data/browse.html'
    return render(request, template, context)

def my_data_view(request):
    head_title = "LUCE"
    # Get first five datasets
    qs = Dataset.objects.all()[:5]
    context = {"head_title": head_title, 
                "dataset_list": qs}
    template = 'data/my_data.html'
    return render(request, template, context)

def detail_view(request, dataset_id):
    obj = get_object_or_404(Dataset, id=dataset_id)
    context = {"object": obj}
    template = 'data/detail.html'
    return render(request, template, context)  
