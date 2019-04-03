import datetime

from django.db.models import Q
from django.shortcuts import render, redirect

from cliente.models import Cliente
from .models import Produto, Pedido, ItemCarrinho
from .forms import FormProduto


def listarProdutos(request):
    produtos = Produto.objects.all()
    args = {'produtos': produtos}
    if request.COOKIES.get('carrinho'):
        carrinho = Pedido.objects.filter(id=request.COOKIES['carrinho']).get()
        itemsCarrinho = ItemCarrinho.objects.filter(carrinho=carrinho).all()
        quantidade=0
        for x in itemsCarrinho:
            quantidade+=x.quantidade
        args['quantidade'] = quantidade
    return render(request, 'produtos.html', args)


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
    args={}
    produtos = Produto.objects.filter(nome__icontains=nome).all()
    args['produtos'] = produtos
    if request.COOKIES['carrinho']:
        carrinho = Pedido.objects.filter(id=request.COOKIES['carrinho']).get()
        itemsCarrinho = ItemCarrinho.objects.filter(carrinho=carrinho).all()
        quantidade=0
        for x in itemsCarrinho:
            quantidade+=x.quantidade
        args['quantidade'] = quantidade
    return render(request, 'produtos.html', args)


def adicionarCarrinho(request, id):
    produto = Produto.objects.filter(id=id).get()
    carrinho = Pedido.objects.filter(id=request.COOKIES['carrinho']).get()
    criterio1 = Q(produto=produto)
    criterio2 = Q(carrinho=carrinho)
    if 'cliente' not in request.COOKIES.keys():
        return redirect('loginCliente')
    try:
        itemCarrinho = ItemCarrinho.objects.filter(criterio1 & criterio2).get()
        itemCarrinho.quantidade +=1
        itemCarrinho.save()
        redirect('listarProdutos')
    except ItemCarrinho.DoesNotExist:
        item = ItemCarrinho(produto=produto, carrinho=carrinho, quantidade=1,preco=produto.preco)
        item.save()
    return redirect('listarProdutos')


def listarCarrinho(request):
    carrinho = Pedido.objects.filter(id=request.COOKIES['carrinho']).get()
    itemsCarrinho = ItemCarrinho.objects.filter(carrinho=carrinho).all()
    quantidade = 0
    valorTotal = 0
    args={}
    for x in itemsCarrinho:
        quantidade += x.quantidade
        valorTotal+= x.quantidade*x.preco
    args['valorTotal'] = valorTotal
    args['quantidade'] = quantidade
    args['items']=itemsCarrinho
    return render(request,'carrinho.html', args)


def removerItem(request, id):
    produto = Produto.objects.filter(id=id).get()
    carrinho = Pedido.objects.filter(id=request.COOKIES['carrinho']).get()
    criterio1 = Q(produto=produto)
    criterio2 = Q(carrinho=carrinho)
    itemCarrinho = ItemCarrinho.objects.filter(criterio1 & criterio2).get()
    itemCarrinho.quantidade -=1
    if itemCarrinho.quantidade ==0:
        itemCarrinho.delete()
    else:
        itemCarrinho.save()
    return redirect('listarCarrinho')


def fecharPedido(request):
    carrinho = Pedido.objects.filter(id=request.COOKIES['carrinho']).get()
    itemsCarrinho = ItemCarrinho.objects.filter(carrinho=carrinho).all()

    carrinho.status = "fechado"
    valorTotal = 0
    for x in itemsCarrinho:
        valorTotal += x.quantidade * x.preco
    carrinho.valorTotal = valorTotal
    now = datetime.date.today()
    print(now)
    carrinho.dataFinalizacao = now
    carrinho.save()
    resposta = redirect('listarProdutos')
    cliente = Cliente.objects.filter(id=request.COOKIES['cliente']).get()
    pedido = Pedido(cliente=cliente, status='aberto')
    pedido.save()
    resposta.set_cookie('carrinho', pedido.id)
    return resposta
