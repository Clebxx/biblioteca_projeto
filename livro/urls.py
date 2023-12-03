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
  path('livros/detalhes/<int:pk>', views.livro_detail.as_view(), name='detalhes livro'),
  path('autores/detalhes/<int:pk>', views.autor_detail.as_view(), name='detalhes autor'),
  path('editoras/detalhes/<int:pk>', views.editora_detail.as_view(), name='detalhes editora'),
  path('generos/detalhes/<int:pk>', views.genero_detail.as_view(), name='detalhes genero'),
  path('livros/editar/<int:pk>', views.livro_update.as_view(), name='editar livro'),
  path('autores/editar/<int:pk>', views.autor_update.as_view(), name='editar autor'),
  path('editoras/editar/<int:pk>', views.editora_update.as_view(), name='editar editora'),
  path('generos/editar/<int:pk>', views.genero_update.as_view(), name='editar genero'),
]