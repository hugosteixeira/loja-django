from django.shortcuts import render, redirect
from .models import Produto
from .forms import FormProduto
from decimal import Decimal



def listarProdutos(request):
    produtos = Produto.objects.all()
    return render(request,'produtos.html',{
        'produtos':produtos
    })


def criar_produtos(request):
    form = FormProduto(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listarProdutos')
    return render(request, 'produtosform.html', {
        'form': form
    })


def update_product(request, id):
    produto = Produto.objects.get(id=id)
    form = FormProduto(request.POST or None, instance=produto)

    if form.is_valid():
        form.save()
        return redirect('listarProdutos')

    return render(request, 'produtosform.html', {'form': form, 'produto': produto})


def deletarProdutos(request, id):
    product = Produto.objects.get(id=id)

    if request.method == 'POST':
        product.delete()
        return redirect('listarProdutos')

    return render(request, 'deleteConfirm.html', {'product': product})


def pesquisarProduto(request):
    dados = request.POST.copy()
    nome = dados.get('pesquisa')
    produtos = Produto.objects.filter(nome__icontains=nome).values()
    return render(request,'produtos.html',{
        'produtos':produtos
    })

