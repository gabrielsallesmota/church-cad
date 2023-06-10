from django import forms
from apps.membros.models import Membro


class MembroForms(forms.ModelForm):
    class Meta:
        model = Membro
        exclude = ['id',]
        labels = {
            'nome_completo': 'Nome:',
            'data_nascimento': 'Data de Nascimento:',
            'email': 'Email:',
            'telefone': 'Telefone:',
            'document': 'Documento(CPF):',
            'genero': 'Gênero:',
            'endereco': 'Endereço:',
            'cep': 'CEP:',
            'estado_civil': 'Estado Civil:',
            'data_membro': 'Data de Entrada Igreja:',
            'data_batismo': 'Data de Batismo:',
            'situacao': 'Situação:',
        }
        widgets = {
            'nome_completo': forms.TextInput(attrs={'class': 'form-control'}),
            'data_nascimento': forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'document': forms.TextInput(attrs={'class': 'form-control'}),
            'genero': forms.Select(attrs={'class': 'form-control'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
            'cep': forms.TextInput(attrs={'class': 'form-control'}),
            'estado_civil': forms.Select(attrs={'class': 'form-control'}),
            'data_membro': forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date', 'class': 'form-control', 'input_formats': ['%Y-%m-%d']}),
            'data_batismo': forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date', 'class': 'form-control', 'input_formats': ['%Y-%m-%d']}),
            'situacao': forms.Select(attrs={'class': 'form-control'}),
        }