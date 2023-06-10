from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from apps.membros.models import Membro
from apps.membros.forms import MembroForms



def index(request):
    return render(request, 'membros/index.html')

def cadastro(request):
    #if not request.user.is_authenticated:
        #return redirect('login')
        #messages.error(request, "Usuário nao logado")
        
    form = MembroForms
    if request.method == 'POST':
        form = MembroForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Novo Memebro Cadastrado!")
            return redirect('index')

    return render(request, 'membros/cadastro.html', {'form': form})


def consulta(request):
    filtro_nome = request.GET.get('nome', '')

    membros = Membro.objects.all()

    if filtro_nome:
        membros = membros.filter(nome_completo__icontains=filtro_nome)

    return render(request, 'membros/consulta.html', {'membros': membros, 'filtro_nome': filtro_nome})


def editar(request, id):
    membro = get_object_or_404(Membro, id=id)

    if request.method == 'POST':
        form = MembroForms(request.POST, request.FILES, instance=membro)
        if form.is_valid():
            form.save()
            return redirect('consulta')
    else:
        form = MembroForms(instance=membro)

    return render(request, 'membros/editar.html', {'form': form, 'membro': membro})


def excluir(request, id):
    membro = get_object_or_404(Membro, id=id)

    if request.method == 'POST':
        membro.delete()
        return redirect('consulta')

    return render(request, 'membros/excluir.html', {'membro': membro})