from django.shortcuts import render, get_object_or_404, redirect

# Generic update view
from django.views.generic.edit import UpdateView
from datastore.models import Dataset
from datastore.forms import DatasetModelForm

# Import Python web3 script
from utils.web3_scripts import deploy_contract, deploy_contract_with_data 




def upload_view(request):
    form = DatasetModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        # Obtain data from form
        obj = form.save(commit=False)
        # Add user attribute
        obj.owner = request.user
        obj.owner_address = request.user.ethereum_public_key

        # Deploy smart contract & retrieve contract address
        contract_address = deploy_contract_with_data(request.user,obj.description,obj.license)
        obj.contract_address = contract_address

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


# class UpdateView(UpdateView):
#     model = Dataset
#     fields = ['title', 'description', 'file', 'license']
#     template_name = 'data/update.html'
#     # success_url = '/register_login'

def update_view(request, dataset_id):
    obj = get_object_or_404(Dataset, id=dataset_id)
    form = DatasetModelForm(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid():
        print("Form is valid")
        # Obtain data from form
        obj = form.save(commit=False)

        # Deploy new smart contract & retrieve contract address
        contract_address = deploy_contract(request.user)
        obj.contract_address = contract_address

        # Save to database
        obj.save()

        # form.save()
        return redirect('/') # (!!!) Redirect
    else:
        print(form)
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
    
