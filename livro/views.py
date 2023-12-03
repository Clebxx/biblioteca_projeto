from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Livro, Autor, Editora, Genero
from django.db.models import ManyToManyField

def get_field_values(instance): # Pegando os campos dos modelos
  field_values = {}
  fields = instance._meta.get_fields(include_hidden=True)

  for field in fields:
    try:
      if isinstance(field, ManyToManyField):
        related_objects = getattr(instance, field.name).all()
        field_values[field.name] = ', '.join(str(obj) for obj in related_objects)
      else:
        field_values[field.name] = getattr(instance, field.name)
    except Exception:
        pass

  return field_values

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

class livro_detail(DetailView):
  model = Livro
  template_name = 'detalhes.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)   
    context['object'] = get_field_values(context['object'])
    context['Model'] = 'livros'
    return context

class autor_detail(DetailView):
  model = Autor
  template_name = 'detalhes.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)   
    context['object'] = get_field_values(context['object'])
    context['Model'] = 'autores'
    return context
  
class editora_detail(DetailView):
  model = Editora
  template_name = 'detalhes.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)   
    context['object'] = get_field_values(context['object'])
    context['Model'] = 'editoras'
    return context
  
class genero_detail(DetailView):
  model = Genero
  template_name = 'detalhes.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)   
    context['object'] = get_field_values(context['object'])
    context['Model'] = 'generos'
    return context

class livro_update(UpdateView):
  model = Livro
  fields = ['nome', 'editora' ,'autores', 'generos']
  template_name = 'forms.html'
  success_url = '/biblioteca/livros'
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['title'] = 'Atualizando Livro'
    return context

class autor_update(UpdateView):
  model = Autor
  fields = ['nome', 'nascimento', 'nacionalidade']
  template_name = 'forms.html'
  success_url = '/biblioteca/autores'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['title'] = 'Atualizando Autor'
    return context
  
class editora_update(UpdateView):
  model = Editora
  fields = ['nome', 'cidade', 'website']
  template_name = 'forms.html'
  success_url = '/biblioteca/editoras'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['title'] = 'Atualizando Editora'
    return context
  
class genero_update(UpdateView):
  model = Genero
  fields = ['nome']
  template_name = 'forms.html'
  success_url = '/biblioteca/generos'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['title'] = 'Atualizando Gênero'
    return context

class livro_delete(DeleteView):
  model = Livro
  success_url = '/biblioteca/livros'
  template_name = 'deletar.html'

class autor_delete(DeleteView):
  model = Autor
  success_url = '/biblioteca/autores'
  template_name = 'deletar.html'

class editora_delete(DeleteView):
  model = Editora
  success_url = '/biblioteca/editoras'
  template_name = 'deletar.html'

class genero_delete(DeleteView):
  model = Genero
  success_url = '/biblioteca/generos'
  template_name = 'deletar.html'