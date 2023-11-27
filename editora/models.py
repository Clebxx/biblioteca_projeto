from django.db import models

class Editora(models.Model):
    nome = models.CharField(max_length=100)
    cidade = models.CharField(max_length=50)
    website = models.URLField()

    def __str__(self):
        return self.nome
