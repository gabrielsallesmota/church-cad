from django.shortcuts import render, redirect
from django.contrib import messages
from apps.ministerios.models import Ministerio
from apps.ministerios.forms import MinisterioForm

def ministerio_consult(request):
    ministerios = Ministerio.objects.all()
    return render(request, 'ministerios/consulta-ministerio.html', {'ministerios': ministerios})


def ministerio_create(request):
    if request.method == 'POST':
        form = MinisterioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ministerio_consult')
    else:
        form = MinisterioForm()
    return render(request, 'ministerios/cadastro-ministerio.html', {'form': form})

def ministerio_update(request, pk):
    ministerio = Ministerio.objects.get(pk=pk)
    if request.method == 'POST':
        form = MinisterioForm(request.POST, instance=ministerio)
        if form.is_valid():
            form.save()
            return redirect('ministerio_consult')
    else:
        form = MinisterioForm(instance=ministerio)
    return render(request, 'ministerios/editar-ministerio.html', {'form': form, 'ministerio': ministerio})

def ministerio_delete(request, pk):
    ministerio = Ministerio.objects.get(pk=pk)
    if request.method == 'POST':
        ministerio.delete()
        return redirect('ministerio_consult')
    return render(request, 'ministerios/excluir-ministerio.html', {'ministerio': ministerio})
