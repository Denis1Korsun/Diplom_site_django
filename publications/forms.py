from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import *
from captcha.fields import CaptchaField


class RegistrationUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')
    captcha = CaptchaField()


class AutorizationUserForm(AuthenticationForm):
    username = forms.CharField(label='Введите имя пользователя (логин)',
                               widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Введите пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class CommunicationWhithCompanyForm(forms.Form):

    first_name = forms.CharField(max_length=100, label='Имя')
    last_name = forms.CharField(max_length=100, required=False, label='Фамилия')
    email = forms.EmailField(max_length=100, label='e-mail')
    phone = forms.CharField(max_length=20, required=False, label='Телефон для связи')
    question = forms.CharField(widget=forms.Textarea(attrs={'cols': 70, 'rows': 15}), label='Ваш вопрос')
    captcha = CaptchaField()


# class ContactForm(forms.ModelForm):
#     class Meta:
#         model = InfoAboutJournal
#         fields = ('address', 'number_one', 'number_two', 'number_three', 'number_four', 'email', 'location_map')
