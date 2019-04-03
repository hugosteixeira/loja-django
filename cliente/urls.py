from django.urls import path
from.views import listarClientes, cliente, criarCliente, loginCliente, logout

urlpatterns = [
    path('cliente', listarClientes, name='listarClientes'),
    path("cliente/<int:codigo>", cliente, name="cliente"),
    path("cliente/new/", criarCliente, name="criarCliente"),
    path("cliente/login", loginCliente, name="loginCliente"),
    path("cliente/logout", logout, name="logout")

]
