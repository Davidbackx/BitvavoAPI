from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=100)
    password = forms.CharField(label="Password", max_length=100, widget=forms.PasswordInput)
class RegisterForm(forms.Form):
    username = forms.CharField(label="Username", max_length=100)
    password = forms.CharField(label="Password", max_length=100, widget=forms.PasswordInput)
    confirm_password = forms.CharField(label="Confirm Password", max_length=100, widget=forms.PasswordInput)
    api_key = forms.CharField(label="API Key", max_length=200)
    api_secret_key  = forms.CharField(label="API Secret Key", max_length=200)
