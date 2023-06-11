from django.db import models
from apps.membros.models import Membro

class GrupoConexao(models.Model):    
    OPCAO_SITUACAO = [
        ("A", "Ativo"),
        ("I", "Inativo")
    ]

    id = models.AutoField(primary_key=True)
    nome_celula = models.CharField(max_length=50)
    endereco = models.CharField(max_length=50)
    lider = models.ForeignKey(
        to=Membro,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="grupos_conexao_lider",
    )
    situacao = models.CharField(max_length=1, choices=OPCAO_SITUACAO, default="")

    def __str__(self):
        return self.nome_celula


class MembrosGrupoConexao(models.Model):
    id = models.AutoField(primary_key=True)
    membro = models.ForeignKey(
        to=Membro,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="grupos_conexao_lider_membros",
    )


    def __str__(self):
        return self.id