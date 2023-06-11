from django import forms
from apps.ministerios.models import Ministerio

class MinisterioForm(forms.ModelForm):
    class Meta:
        model = Ministerio
        exclude = ['id']
        labels = {
            'ministerio': 'Ministério:',
            'membro': 'Membro:',
            'situacao': 'Situação:',
        }
        widgets = {
            'ministerio': forms.Select(attrs={'class': 'form-control'}),
            'membro': forms.Select(attrs={'class': 'form-control'}),
            'situacao': forms.Select(attrs={'class': 'form-control'}),
        }
