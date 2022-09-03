from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users.models import Profile

# to add email to user registration, uncomment sections below
class UserRegisterForm(UserCreationForm):
    
    class Meta:
        model = User
        fields =['username', 'password1', 'password2']


class UserProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ['teacher', 'course']