from django.urls import path
from myapp.views import *

# Create your views here.

urlpatterns = [
    path("", index, name="index"),
    path("listar/", listar, name="listarProduct"),
    path("addProduto/", addProduct, name="adicionarProduct"),
    path("editarProduto/<int:id>", edit, name="editar_item"),
    path("atualizarProduto/<int:id>", update, name="atualizar_item"),
    path("visualizarProduto/<int:id>", read, name="visualizar_item"),
    path("deletarProduto/<int:id>", delete, name="deletar_item"),
    path("cart/", createCart, name="createCart")
]