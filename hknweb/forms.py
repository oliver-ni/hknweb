from django import forms
from hknweb.models import User
from hknweb.models import Profile
from hknweb.alumni.models import Alumnus
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, SetPasswordForm

class SettingsForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('picture', 'private', 'phone_number', 'date_of_birth', 'resume', 'graduation_date')

class SignupForm(UserCreationForm):
     first_name = forms.CharField(max_length=30, required=True)
     last_name = forms.CharField(max_length=30, required=True)
     email = forms.EmailField(max_length=200, required=True)

     class Meta:
          model = User
          fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

class UpdatePasswordForm(SetPasswordForm):

    new_password1 = forms.CharField(max_length=30, required=True, label = "New password")
    new_password1.help_text = ''

class ValidPasswordForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('password',)
