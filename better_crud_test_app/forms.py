from django import forms
from .models import DataTable


class DataForm(forms.ModelForm):
    class Meta:
        model = DataTable

        fields = ['text']

        widgets = {
            'text': forms.TextInput(attrs={'placeholder': 'Enter text...'})
        }