from django.shortcuts import render, get_object_or_404
from .models import Autor
from .forms import AutorForm
from django.shortcuts import redirect

def autor_list(request):
    autores = Autor.objects.all()
    return render(request, 'autor/autor_list.html', {'autores': autores})

def autor_detail(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    return render(request, 'autor/autor_detail.html', {'autor': autor})

def autor_new(request):
    if request.method == "POST":
        form = AutorForm(request.POST)
        if form.is_valid():
            autor = form.save(commit=False)
            autor.save()
            return redirect('autor_detail', pk=autor.pk)
    else:
        form = AutorForm()
    return render(request, 'autor/autor_edit.html', {'form': form})

def autor_edit(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == "POST":
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            autor = form.save(commit=False)
            autor.save()
            return redirect('autor_detail', pk=autor.pk)
    else:
        form = AutorForm(instance=autor)
    return render(request, 'autor/autor_edit.html', {'form': form})

def autor_delete(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    autor.delete()
    return redirect('autor_list')
