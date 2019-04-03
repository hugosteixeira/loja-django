from django.db.models import Q
from django.http import HttpResponse
from django.contrib import messages
import json

from django.shortcuts import render, redirect
from .models import Cliente
from .forms import FormCliente


def listarClientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'listarClientes.html', {
        'clientes':clientes
    })


def cliente(request,codigo):
    cliente = Cliente.objects.get(id=codigo)
    return render(request, 'cliente.html', {
        'cliente':cliente
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
        cliente = Cliente.objects.filter(email & senha).values()
        if not cliente:
            return render(request, 'login.html', {'error': 'Usuário ou senha invalidos.'})
        response = redirect('listarProdutos')
        response.set_cookie("cliente", cliente[0]['id'])
        return response
    return render(request, 'login.html')



