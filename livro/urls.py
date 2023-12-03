from django.urls import path
from . import views

urlpatterns = [
  path('', views.home.as_view(), name='Home page'),
  path('livros', views.livro_list.as_view(), name='livros'),
  path('autores', views.autor_list.as_view(), name='autores'),
  path('editoras', views.editora_list.as_view(), name='editoras'),
  path('generos', views.genero_list.as_view(), name='generos'),
  path('livros/adicionar', views.livro_add.as_view(), name='adicionar livro'),
  path('autores/adicionar', views.autor_add.as_view(), name='adicionar autor'),
  path('editoras/adicionar', views.editora_add.as_view(), name='adicionar editora'),
  path('generos/adicionar', views.genero_add.as_view(), name='adicionar genero'),
]