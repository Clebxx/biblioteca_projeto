from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    nascimento = models.DateField()
    nacionalidade = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"
