from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Page

class PageForm(forms.ModelForm):

    class Meta:
        model = Page
        fields = ['title', 'content', 'order']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título de la página'}),
            'content': CKEditorWidget(),
            'order': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Orden (ej: 1, 2, 3...)'}),
        }
        labels = {
            'title': '',
            'content': '',
            'order': '',
        }
