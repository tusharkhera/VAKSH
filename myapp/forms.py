from django import forms
from django.contrib.auth import models
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm, PasswordResetForm, SetPasswordForm, UserChangeForm
from django.contrib.auth.models import User
from django.forms import fields
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth import password_validation
from .models import Customer


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':''}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':''}))
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class':''}))
    class Meta :
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'password1', 'password2']
        labels = {'email': 'Email', 'first_name':'First Name', 'last_name':'Last Name'}
        widgets = {'username': forms.TextInput(attrs={'class':''})}

class LogInForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={"autofocus":True, 'class':''}))
    password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class':''}))

class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=_("Old Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'auto-focus':True}))
    new_password1 = forms.CharField(label=_("New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password'}))
    new_password2 = forms.CharField(label=_("Confirm New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password'}))

class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label=_("Email"), max_length=254, widget=forms.EmailInput(attrs={'autocomplete':'email'}))

class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label=_("New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password'}),
    help_text = password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_("Confirm New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password'}))

class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'contact', 'locality', 'city', 'zipcode', 'state']


class ProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'email':'Email'}