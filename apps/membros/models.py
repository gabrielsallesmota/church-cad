from django.db import models


class Membro(models.Model):
        
    OPCOES_GENERO = [
        ("M", "Masculino"),
        ("F", "Feminino")
    ]

    OPCOES_ATIVO = [
        ("A", "Ativo"),
        ("I", "Inativo")
    ]

    OPCOES_ESTADO_CIVIL = [
        ("S", "Solteiro(a)"),
        ("C", "Casado(a)"),
        ("V", "Viuvo(a)")
    ]

    id = models.AutoField(primary_key=True)    
    nome_completo = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    email = models.CharField(max_length=40)
    telefone = models.CharField(max_length=12)
    document = models.CharField(max_length=11)
    genero = models.CharField(max_length=1, choices=OPCOES_GENERO, default="")
    endereco = models.CharField(max_length=100)
    cep = models.CharField(max_length=8)
    estado_civil = models.CharField(max_length=8, choices=OPCOES_ESTADO_CIVIL, default="")
    data_membro = models.DateField()
    data_batismo = models.DateField()
    situacao = models.CharField(max_length=1, choices=OPCOES_ATIVO, default="")

    def __str__(self):
        return self.nome_completo
