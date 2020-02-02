from django import forms
from django.forms import ModelForm
from .models import stdresult
from .models import stdnotice
from django.db import models
from django.forms import ModelForm



class UserLoginForms(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))



class BookForm(ModelForm):
    class Meta:
        model = stdresult
        fields = '__all__'

class NoticeForm(ModelForm):
    class Meta:
        model = stdnotice
        fields = '__all__'