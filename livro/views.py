from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
from .models import Livro, Autor, Editora, Genero

class home(View):
    def get(self, request):
        return render(request, 'home-page.html')

class livro_list(ListView):
    model = Livro
    
    def get(self, request):
        return render(request, 'objetos.html', {'objects': Livro.objects.all(), 'Model': 'livros'})

class autor_list(ListView):
    model = Autor

    def get(self, request):
        return render(request, 'objetos.html', {'objects': Autor.objects.all(), 'Model': 'autores'})

class editora_list(ListView):
    model = Editora

    def get(self, request):
        return render(request, 'objetos.html', {'objects': Editora.objects.all(), 'Model': 'editoras'})
    
class genero_list(ListView):
    model = Genero

    def get(self, request):
        return render(request, 'objetos.html', {'objects': Genero.objects.all(), 'Model': 'generos'})