from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict

from .forms import UserRegistrationForm, ClientInformationForm

from .models import ClientInformation

# Create your views here.

@login_required
def dashboard(request):
    client_info, found = ClientInformation.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ClientInformationForm(request.POST, instance=client_info)
        form.save()
    else:
        form = ClientInformationForm(initial=client_info.__dict__)
    
    return render(request, 'account/dashboard.html', {'user': request.user.username, 'form': form})


# def login(request):
#     if request.method == 'POST':
#         pass
#     else:
#         pass
#     return render(request, 'account/login.html')


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})