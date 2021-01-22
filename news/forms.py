from django import forms
from django.contrib.auth.models import User
from .models import News
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# Форма не связанная с моделью

class ContactForm(forms.Form):
    subject = forms.CharField(label='Тема', widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label='Text', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))


# class NewsForm(forms.Form):
#     title = forms.CharField(max_length=50, label='Название', widget=forms.TextInput(attrs={
#         'class': 'form-control'
#     }))
#     content = forms.CharField(max_length=1000, label='Текст', required=False, widget=forms.Textarea(attrs={
#         'class': 'form-control',
#         'rows': 5
#     }))
#     is_published = forms.BooleanField(label='Опубликовать', initial=True)
#     category = forms.ModelChoiceField(empty_label="Выберите категорию", queryset=Category.objects.all(),
#                                       label='Категория', widget=forms.Select(attrs={'class': 'form-control'}))
# Форма связанная с моделью

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    username = forms.CharField(label='username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='password again', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        # fields = '__all__'
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'category': forms.Select(attrs={'class': 'form-control'})

        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Название не должно начинаться с цифры')
        return title
