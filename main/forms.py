from django import forms

from main.models import IHA


class IHAForm(forms.ModelForm):
    class Meta:
        model = IHA
        fields = [
            'marka',
            'model',
            'agirlik',
            'category',
        ]
        widgets = {
            'marka': forms.TextInput(attrs={'class': 'form-control'}),
            'model': forms.TextInput(attrs={'class': 'form-control'}),
            'agirlik': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'marka': 'Marka',
            'model': 'Model',
            'agirlik': 'Ağırlık',
            'category': 'Kategori',
        }