from django.db import models
from apps.membros.models import Membro

class Ministerio(models.Model):
    OPCAO_MINISTERIO = [
        ("1", "Pastoral"),
        ("2", "Louvor"),
        ("3", "Dança"),
        ("4", "Atmosfera"),
        ("5", "Royal Kids"),
        ("6", "Teens"),
        ("7", "Fé em Ação"),
    ]
    
    OPCAO_SITUACAO = [
        ("A", "Ativo"),
        ("I", "Inativo")
    ]

    id = models.AutoField(primary_key=True)
    ministerio = models.CharField(max_length=2, choices=OPCAO_MINISTERIO, default="")
    membro = models.ForeignKey(
        to=Membro,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="ministerios",
    )
    situacao = models.CharField(max_length=1, choices=OPCAO_SITUACAO, default="")

    def __str__(self):
        return self.id