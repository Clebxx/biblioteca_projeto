from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=50)
    nascimento = models.DateField()
    nacionalidade = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nome}"

class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    autores = models.ManyToManyField('Autor')
    editora = models.ForeignKey('Editora', on_delete=models.CASCADE)
    generos = models.ManyToManyField('Genero')

    def __str__(self):
        return self.titulo
    
class Genero(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
        
class Editora(models.Model):
    nome = models.CharField(max_length=100)
    cidade = models.CharField(max_length=50)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.nome
