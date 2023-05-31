from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django import forms

from .models import User


class SingUpForm(forms.ModelForm):
    phone_number = forms.CharField(max_length=12, widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model=User
        fields = ('phone_number', 'first_name', 'last_name', 'password', 'show_password')

    # def __init__(self, *args, **kwargs) -> None:
    #     super(SingUpForm,self).__init__(*args, **kwargs)
    #
    #     self.fields['phone_number'].widget.attrs['class']='form-control'
    #     self.fields['password'].widget.attrs['class']='form-control'
    #     self.fields['show_password'].widget.attrs['class']='form-control'