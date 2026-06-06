from django import forms
from .models import Quotation

class QuotationForm(forms.ModelForm):
    class Meta:
        model = Quotation
        fields = ['price', 'delivery_timeline', 'notes']
        widgets = {
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 5000.00', 'min': '0.01'}),
            'delivery_timeline': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 10', 'min': '1'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Optional notes, terms, etc.'}),
        }
