from django import forms
from django.contrib.auth.models import User

from .models import ClientInformation
# from .models import UserProfile

# class ClientLoginForm(forms.ModelForm):
#     password = forms.CharField(label='Password', widget=forms.PasswordInput)

#     class Meta:
#         model = UserProfile
#         fields = ['username']


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Passwords don't match.")
        return cd['password2']


class ClientInformationForm(forms.ModelForm):

    class Meta:
        model = ClientInformation
        fields = ['case_type', 'residence_state', 'incident_state', 'incident_description']
