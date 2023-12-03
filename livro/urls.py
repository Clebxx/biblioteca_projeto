from django.urls import path
from . import views

urlpatterns = [
  path('', views.home.as_view(), name='Home page'),
  path('livros', views.livro_list.as_view(), name='livros'),
  path('autores', views.autor_list.as_view(), name='autores'),
  path('editoras', views.editora_list.as_view(), name='editoras'),
  path('generos', views.genero_list.as_view(), name='generos'),
]