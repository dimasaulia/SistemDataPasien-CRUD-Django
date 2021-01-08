from django import forms
from .models import DataPasien

class PasienForms(forms.ModelForm):
    class Meta:
        model   = DataPasien
        fields  = (
            'nama',
            'alamat',
            'kota',
            'no_telepon',
        )
