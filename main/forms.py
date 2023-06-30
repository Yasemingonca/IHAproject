from django import forms

from main.models import IHA, RentalRecord


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


class RentalForm(forms.Form):
    start_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'class': 'form-control'}),
        label='Başlangıç Tarihi'
    )
    end_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'class': 'form-control'}),
        label='Bitiş Tarihi'
    )

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")

        if start_date and end_date and start_date > end_date:
            raise forms.ValidationError("Başlangıç tarihi bitiş tarihinden büyük olamaz")
