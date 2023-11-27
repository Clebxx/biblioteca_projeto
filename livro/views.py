from django.shortcuts import render, get_object_or_404
from .models import Livro
from .forms import LivroForm
from django.shortcuts import redirect

def livro_list(request):
    livros = Livro.objects.all()
    return render(request, 'livro/livro_list.html', {'livros': livros})

def livro_detail(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    return render(request, 'livro/livro_detail.html', {'livro': livro})

def livro_new(request):
    if request.method == "POST":
        form = LivroForm(request.POST)
        if form.is_valid():
            livro = form.save(commit=False)
            livro.save()
            return redirect('livro_detail', pk=livro.pk)
    else:
        form = LivroForm()
    return render(request, 'livro/livro_edit.html', {'form': form})

def livro_edit(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == "POST":
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            livro = form.save(commit=False)
            livro.save()
            return redirect('livro_detail', pk=livro.pk)
    else:
        form = LivroForm(instance=livro)
    return render(request, 'livro/livro_edit.html', {'form': form})

def livro_delete(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    livro.delete()
    return redirect('livro_list')
