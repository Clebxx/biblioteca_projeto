from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .models import Livro, Autor, Editora, Genero

class home(View):
    def get(self, request):
        return render(request, 'home-page.html')

class livro_list(ListView):
    model = Livro
    
    def get(self, request):
        print(Livro.objects.all())

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

class livro_add(CreateView):
  model = Livro
  fields = ['nome', 'editora' ,'autores', 'generos']
  template_name = 'forms.html'
  success_url = '/biblioteca/livros'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['title'] = 'Adicionando Livro'
    return context

class autor_add(CreateView):
  model = Autor
  fields = ['nome', 'nascimento', 'nacionalidade']
  template_name = 'forms.html'
  success_url = '/biblioteca/autores'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['title'] = 'Adicionando Autor'
    return context
  
class editora_add(CreateView):
  model = Editora
  fields = ['nome', 'cidade', 'website']
  template_name = 'forms.html'
  success_url = '/biblioteca/editoras'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['title'] = 'Adicionando Editora'
    return context

class genero_add(CreateView):
  model = Genero
  fields = ['nome']
  template_name = 'forms.html'
  success_url = '/biblioteca/generos'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['title'] = 'Adicionando Gênero'
    return context