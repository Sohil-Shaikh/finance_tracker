from django import forms
from .models import Income


class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['title', 'category', 'amount', 'description', 'date']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Income Title'
            }),

            'category': forms.Select(attrs={
                'class': 'form-select'
            }),

            'amount': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Amount'
            }),

            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            }),

            'date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
        }