from django.shortcuts import render, get_object_or_404, redirect

from datastore.models import Dataset
from datastore.forms import DatasetModelForm


def upload_view(request):
    form = DatasetModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        # Obtain data from form
        obj = form.save(commit=False)
        # Add user attribute
        obj.owner = request.user
        obj.owner_address = request.user.ethereum_public_key
        # Save to database
        obj.save()

        # -> Data has been submitted and stored
        # Display a new, empty form
        form = DatasetModelForm()

        # (!!!) Redirect to subsequent page
        # return redirect('/upload_success')
    context = {
            'form': form
                }
    template = 'data/upload.html'
    return render(request, template, context)


def browse_view(request):
    head_title = "LUCE"
    # Get all datasets
    qs = Dataset.objects.all()
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
    context = {"dataset": obj}
    template = 'data/detail.html'
    return render(request, template, context)  

def update_view(request, dataset_id):
    obj = get_object_or_404(Dataset, id=dataset_id)
    form = DatasetModelForm(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid():
        print("Form is valid")
        form.save()
        return redirect('/') # (!!!) Redirect
    else:
        print("Form is not valid")
    context = {
            'form': form,
            'dataset': obj,
                }
    template = 'data/update.html'
    return render(request, template, context)

def delete_view(request, dataset_id):
    obj = get_object_or_404(Dataset, id=dataset_id)
    if request.method == "POST":
        obj.delete()
        return redirect("/")
    context = {"dataset": obj}
    template = 'data/delete.html'
    return render(request, template, context)
    
