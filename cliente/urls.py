from django.urls import path
from.views import listarClientes, cliente, criarCliente, loginCliente

urlpatterns = [
    path('cliente', listarClientes, name='listarClientes'),
    path("cliente/<int:codigo>", cliente, name="cliente"),
    path("cliente/new/", criarCliente, name="criarCliente"),
    path("cliente/login", loginCliente, name="loginCliente")

]
