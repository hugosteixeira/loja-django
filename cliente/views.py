from django.db.models import Q
from django.contrib import messages

from django.shortcuts import render, redirect

from produto.models import Pedido
from .models import Cliente
from .forms import FormCliente


def listarClientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'listarClientes.html', {
        'clientes': clientes
    })


def cliente(request, codigo):
    cliente = Cliente.objects.get(id=codigo)
    return render(request, 'cliente.html', {
        'cliente': cliente
    })


def criarCliente(request):
    form = FormCliente(request.POST or None)
    if form.is_valid():
        cliente = form.save()
        response = redirect('listarClientes')
        response.set_cookie("cliente", cliente.id)
        return response
    messages.info(request, form.errors.as_text())
    return render(request, 'login.html', {
        'form': form
    })


def loginCliente(request):
    if request.method == "POST":
        dados = request.POST.copy()
        email = Q(email=dados.get('email'))
        senha = Q(senha=dados.get('senha'))
        cliente = Cliente.objects.filter(email & senha).get()
        if not cliente:
            return render(request, 'login.html', {'error': 'Usuário ou senha invalidos.'})
        response = redirect('listarProdutos')
        response.set_cookie("cliente", cliente.id)
        response = gerarCarrinho(cliente, response)
        return response
    return render(request, 'login.html')


def gerarCarrinho(cliente,resposta):
    pedido = Pedido(cliente=cliente, status='aberto')
    pedido.save()
    resposta.set_cookie('carrinho', pedido.id)
    return resposta


def logout(request):
    response = redirect('listarProdutos')
    response.delete_cookie('cliente')
    return response


def meusPedidos(request):
    cliente = Cliente.objects.filter(id=request.COOKIES['cliente']).get()
    pedidos = Pedido.objects.filter(cliente=cliente).all()
    return render(request,'meusPedidos.html')