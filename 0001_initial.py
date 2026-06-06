from django import forms
from .models import RFQ
from vendors.models import Vendor

class RFQForm(forms.ModelForm):
    assigned_vendors = forms.ModelMultipleChoiceField(
        queryset=Vendor.objects.filter(status='active'),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
        required=True,
        help_text="Select one or more active vendors to receive this RFQ."
    )

    class Meta:
        model = RFQ
        fields = ['title', 'description', 'product_name', 'quantity', 'deadline', 'attachment', 'assigned_vendors', 'status']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'product_name': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'deadline': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'attachment': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }
