from django.urls import path
from .views import listarClientes, cliente, criarCliente, loginCliente, logout, meusPedidos, meuPedido

urlpatterns = [
    path('cliente', listarClientes, name='listarClientes'),
    path("cliente/<int:codigo>", cliente, name="cliente"),
    path("cliente/new/", criarCliente, name="criarCliente"),
    path("cliente/login", loginCliente, name="loginCliente"),
    path("cliente/logout", logout, name="logout"),
    path("cliente/meuspedidos", meusPedidos, name="meusPedidos"),
    path("cliente/pedido/<int:id>", meuPedido, name='meuPedido')

]
