from django.urls import path
from .views import listarProdutos, criar_produtos,update_product,deletarProdutos,pesquisarProduto

urlpatterns =[
    path('', listarProdutos,name='listarProdutos'),
    path('produtos/pesquisar',pesquisarProduto,name='pesquisarProduto'),
    path('produto/cadastrar/', criar_produtos, name='criar_produtos'),
    path('produto/update/<int:id>/', update_product, name='update_product'),
    path('produto/delete/<int:id>/', deletarProdutos, name='deletarProdutos'),
]
