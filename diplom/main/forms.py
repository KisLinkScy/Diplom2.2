from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Services


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class SignUpForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)
        self.fields['username'].label = ""
        self.fields['email'].label = ""
        self.fields['password1'].label = ""
        self.fields['password2'].label = ""
        self.fields['username'].widget.attrs.update(
            {'class': 'form-item form-control'})
        self.fields['email'].widget.attrs.update(
            {'class': 'form-item form-control'})
        self.fields['password1'].widget.attrs.update(
            {'class': 'form-item form-control'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-item form-control'})

        # giving place holders to fields
        self.fields['username'].widget.attrs.update(
            {'placeholder': 'Имя пользователя*'})
        self.fields['email'].widget.attrs.update(
            {'placeholder': 'E-mail*'})
        self.fields['password1'].widget.attrs.update(
            {'placeholder': 'Пароль*'})
        self.fields['password2'].widget.attrs.update(
            {'placeholder': 'Повторите пароль*'})

        for text in ['username', 'password1', 'password2']:
            self.fields[text].help_text = None
