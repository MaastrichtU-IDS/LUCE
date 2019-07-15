from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from django.utils.http import is_safe_url

# Access to Dataset model
from datastore.models import Dataset

# Access to forms
from accounts.forms import RegisterForm, LoginForm

# For login view:
from django.contrib.auth import authenticate, login, get_user_model

# For class-based views:
from django.views.generic import CreateView, FormView

# For redirect after form submission
from django.shortcuts import redirect

# Import Python web3 scripts
from utils.web3_scripts import create_wallet, fund_wallet, deploy_contract, assign_address

def home_page(request):
    head_title = "LUCE"
    # Get first five datasets
    qs = Dataset.objects.all()[:5]
    context = {"head_title": head_title, 
                "dataset_list": qs}
    template = 'home.html'
    return render(request, template, context)


# Obtain access to our (custom) user model
# User = get_user_model()


# Class-Based View that handles a lot of detail automatically for us:
class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = '/register_login' # Maybe better '/login' with success message and next steps..
    # Can use register/login flow to direct user through page experience.

# Old function-based view
# def register_view(request):
#     form = RegisterForm(request.POST or None)
#     context = {"form": form}
#     if form.is_valid():
#         form.save()
#     template = 'accounts/register.html'
#     return render(request, template, context)

class LoginView(FormView):
    form_class = LoginForm
    template_name = 'accounts/login.html'
    success_url = '/'

    def form_valid(self, form):
        request = self.request
        next_ = request.GET.get('next')
        next_post = request.POST.get('next')
        redirect_path = next_ or next_post or None


        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            try:
                del request.session['guest_email_id']
            except:
                pass
            if is_safe_url(redirect_path, request.get_host()):
                return redirect(redirect_path)
            else:
                return redirect('/')
        return super(LoginView, self).form_invalid(form)


class LoginView_PostReg(FormView):
    form_class = LoginForm
    template_name = 'accounts/login_post_reg.html'
    success_url = '/'

    def form_valid(self, form):
        request = self.request
        next_ = request.GET.get('next')
        next_post = request.POST.get('next')
        redirect_path = next_ or next_post or None


        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            try:
                del request.session['guest_email_id']
            except:
                pass
            if is_safe_url(redirect_path, request.get_host()):
                return redirect(redirect_path)
            else:
                return redirect('/')
        return super(LoginView, self).form_invalid(form)


# Available scripts:
# create_wallet, fund_wallet, deploy_contract, assign_address

def dev_view(request):

    if(request.GET.get('assign_address')):
        # Pass request into web3 script

        current_user = request.user
        current_user = assign_address(current_user)
        # Save already takes place while assigning address
        # current_user.save()
        print(current_user)
        print(current_user.ethereum_public_key)
        print("Address was assigned to current user.")

    if(request.GET.get('mybtn_2')):
        create_wallet()
        print("Second button was pressed")

    if(request.GET.get('mybtn_4')):
        print("Forth button was pressed")        

    if(request.GET.get('mybtn')):
        print( int(request.GET.get('mytextbox')) ) # or any other function

    context = {}
    template = 'dev.html'
    return render(request, template, context)
    