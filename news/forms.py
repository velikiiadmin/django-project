from django import forms
from .models import Category


class NewsForm(forms.Form):
    title = forms.CharField(max_length=50, label='Название', widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    content = forms.CharField(max_length=1000, label='Текст', required=False, widget=forms.Textarea(attrs={
        'class': 'form-control',
        'rows': 5
    }))
    is_published = forms.BooleanField(label='Опубликовать', initial=True)
    category = forms.ModelChoiceField(empty_label="Выберите категорию", queryset=Category.objects.all(),
                                      label='Категория', widget=forms.Select(attrs={'class': 'form-control'}))
