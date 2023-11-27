from django.db import models
from autor.models import Autor

class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    autores = models.ManyToManyField(Autor)
    editora = models.ForeignKey('editora.Editora', on_delete=models.CASCADE)
    generos = models.ManyToManyField('genero.Genero')

    def __str__(self):
        return self.titulo
