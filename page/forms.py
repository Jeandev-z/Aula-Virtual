from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'form-control','type':'text','name': 'email','placeholder':'Email'}), 
        label='Email')     
    password1 = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control','type':'password','name': 'password1','placeholder':'Contraseña'}), 
        label='Password')

    password2 = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control','type':'password','name': 'password2','placeholder':'Contraseña de confirmación'}), 
        label='Password')
        
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email',)

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'form-control','type':'text','name': 'email','placeholder':'Email'}), 
        label='Email')
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class':'form-control','type':'password', 'name': 'password','placeholder':'Password'}),
        label='Password')
    class Meta:
        model = User
        fields = ('email', 'password',)
        widgets = {
        'password': forms.PasswordInput(),
    }