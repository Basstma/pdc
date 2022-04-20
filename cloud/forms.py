from django import forms
from .models import *


class FileObjectForm(forms.ModelForm):

    class Meta:
        model = FileObject
        fields = ('filename', 'file', 'content_type')


class EmbeddedObjectForm(forms.ModelForm):

    class Meta:
        model = EmbededObject
        fields = ('filename', 'content_type', 'content')

        widgets = {
            'filename': forms.TextInput(attrs={'class': 'form-control'}),
            'content_type': forms.Select(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }