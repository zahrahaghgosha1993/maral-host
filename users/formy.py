from django import forms

from users.models import MaralUser


class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)


class LoginUserForm(forms.ModelForm):
    class Meta:
        model = MaralUser
        fields = ['email', 'password']
