from django.shortcuts import render, get_object_or_404, redirect
from .models import GrupoConexao
from .forms import GrupoConexaoForm

def grupo_conexao_list(request):
    grupos_conexao = GrupoConexao.objects.all()
    return render(request, 'grupos_conexao/listar-gc.html', {'grupos_conexao': grupos_conexao})

def grupo_conexao_create(request):
    form = GrupoConexaoForm()
    if request.method == 'POST':
        form = GrupoConexaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('grupo_conexao_list')
    return render(request, 'grupos_conexao/criar-gc.html', {'form': form})

def grupo_conexao_update(request, pk):
    grupo_conexao = get_object_or_404(GrupoConexao, pk=pk)
    form = GrupoConexaoForm(instance=grupo_conexao)
    if request.method == 'POST':
        form = GrupoConexaoForm(request.POST, instance=grupo_conexao)
        if form.is_valid():
            form.save()
            return redirect('grupo_conexao_list')
    return render(request, 'grupos_conexao/editar-gc.html', {'form': form, 'grupo_conexao': grupo_conexao})

def grupo_conexao_delete(request, pk):
    grupo_conexao = get_object_or_404(GrupoConexao, pk=pk)
    if request.method == 'POST':
        grupo_conexao.delete()
        return redirect('grupo_conexao_list')
    return render(request, 'grupos_conexao/deletar-gc.html', {'grupo_conexao': grupo_conexao})
