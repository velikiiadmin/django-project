from django import forms
from .models import News
import re
from django.core.exceptions import ValidationError


# Форма не связанная с моделью
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
        title = self.changed_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Название не должно начинаться с цифры')
        return title
