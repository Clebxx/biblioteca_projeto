from django.shortcuts import render, get_object_or_404
from .models import Editora
from .forms import EditoraForm
from django.shortcuts import redirect

def editora_list(request):
    editoras = Editora.objects.all()
    return render(request, 'editora/editora_list.html', {'editoras': editoras})

def editora_detail(request, pk):
    editora = get_object_or_404(Editora, pk=pk)
    return render(request, 'editora/editora_detail.html', {'editora': editora})

def editora_new(request):
    if request.method == "POST":
        form = EditoraForm(request.POST)
        if form.is_valid():
            editora = form.save(commit=False)
            editora.save()
            return redirect('editora_detail', pk=editora.pk)
    else:
        form = EditoraForm()
    return render(request, 'editora/editora_edit.html', {'form': form})

def editora_edit(request, pk):
    editora = get_object_or_404(Editora, pk=pk)
    if request.method == "POST":
        form = EditoraForm(request.POST, instance=editora)
        if form.is_valid():
            editora = form.save(commit=False)
            editora.save()
            return redirect('editora_detail', pk=editora.pk)
    else:
        form = EditoraForm(instance=editora)
    return render(request, 'editora/editora_edit.html', {'form': form})

def editora_delete(request, pk):
    editora = get_object_or_404(Editora, pk=pk)
    editora.delete()
    return redirect('editora_list')
