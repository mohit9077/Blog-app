from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile



class UserRegisterForm(UserCreationForm):

    email=forms.EmailField()

    class Meta:
        model = User  ## when form.save is executed than it gets save in user model
        fields=['username','email','password1','password2']    ## this gives the fields you have to display 



class UserUpdate(forms.ModelForm):

    email=forms.EmailField()

    class Meta:
        model = User  
        fields=['username','email']


class ProfileUpdate(forms.ModelForm):
    class Meta:
        model =Profile

        fields=['image']
