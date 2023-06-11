from django import forms
from apps.grupo_conexao.models import GrupoConexao, MembrosGrupoConexao

class GrupoConexaoForm(forms.ModelForm):
    class Meta:
        model = GrupoConexao
        exclude = ['id']
        labels = {
            'nome_celula': 'Nome da Célula:',
            'endereco': 'Endereço:',
            'lider': 'Líder:',
            'situacao': 'Situação:',
        }
        widgets = {
            'nome_celula': forms.TextInput(attrs={'class': 'form-control'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
            'lider': forms.Select(attrs={'class': 'form-control'}),
            'situacao': forms.Select(attrs={'class': 'form-control'}),
        }


class MembrosGrupoConexaoForm(forms.ModelForm):
    class Meta:
        model = MembrosGrupoConexao
        exclude = ['id']
        labels = {
            'membro': 'Membro:',
        }
        widgets = {
            'membro': forms.Select(attrs={'class': 'form-control'}),
        }
