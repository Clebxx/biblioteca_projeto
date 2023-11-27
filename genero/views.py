from django.shortcuts import render, get_object_or_404
from .models import Genero
from .forms import GeneroForm
from django.shortcuts import redirect

def genero_list(request):
    generos = Genero.objects.all()
    return render(request, 'genero/genero_list.html', {'generos': generos})

def genero_detail(request, pk):
    genero = get_object_or_404(Genero, pk=pk)
    return render(request, 'genero/genero_detail.html', {'genero': genero})

def genero_new(request):
    if request.method == "POST":
        form = GeneroForm(request.POST)
        if form.is_valid():
            genero = form.save(commit=False)
            genero.save()
            return redirect('genero_detail', pk=genero.pk)
    else:
        form = GeneroForm()
    return render(request, 'genero/genero_edit.html', {'form': form})

def genero_edit(request, pk):
    genero = get_object_or_404(Genero, pk=pk)
    if request.method == "POST":
        form = GeneroForm(request.POST, instance=genero)
        if form.is_valid():
            genero = form.save(commit=False)
            genero.save()
            return redirect('genero_detail', pk=genero.pk)
    else:
        form = GeneroForm(instance=genero)
    return render(request, 'genero/genero_edit.html', {'form': form})

def genero_delete(request, pk):
    genero = get_object_or_404(Genero, pk=pk)
    genero.delete()
    return redirect('genero_list')
