from django import forms
from .models import Expense


class ExpenseForm(forms.ModelForm):

    class Meta:
        model = Expense

        fields = [
            'title',
            'category',
            'amount',
            'description',
            'date'
        ]

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'category': forms.Select(attrs={
                'class': 'form-select'
            }),

            'amount': forms.NumberInput(attrs={
                'class': 'form-control'
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