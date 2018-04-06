# -*- coding: utf-8 -*-
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms


class UesrForm(UserCreationForm):
    carNum = forms.CharField(required=True)
    email = forms.EmailField(label='Enter email')
    
class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30, 
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))
