from django import forms

class SignupForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    age = forms.IntegerField()
    name = forms.CharField()
    email = forms.EmailField()
    phone_number = forms.CharField()
    security_question = forms.CharField()
    security_answer = forms.CharField()

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

class ForgotPasswordForm(forms.Form):
    username = forms.CharField()
    security_question = forms.CharField()
    security_answer = forms.CharField()
    # new_password = forms.CharField(widget=forms.PasswordInput())