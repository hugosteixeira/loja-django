from django.urls import path
from .views import listarProdutos, criar_produtos, update_product, deletarProdutos, pesquisarProduto, adicionarCarrinho, \
    listarCarrinho, removerItem, fecharPedido

urlpatterns = [
    path('', listarProdutos, name='listarProdutos'),
    path('produtos/pesquisar', pesquisarProduto, name='pesquisarProduto'),
    path('produto/cadastrar/', criar_produtos, name='criar_produtos'),
    path('produto/update/<int:id>/', update_product, name='update_product'),
    path('produto/delete/<int:id>/', deletarProdutos, name='deletarProdutos'),
    path('produto/add/<int:id>/', adicionarCarrinho, name='adicionarCarrinho'),
    path('produto/carrinho', listarCarrinho, name='listarCarrinho'),
    path('produto/tirar/<int:id>', removerItem, name='removerItem'),
    path('produto/fechar/', fecharPedido, name='fecharPedido'),


]
