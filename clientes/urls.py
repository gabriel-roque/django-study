from django.urls import path
from .views import *

urlpatterns = [
    path('', listarClientes, name="listar.cliente"),
    path('cliente/novo/', armazenarCliente, name="novo.cliente"),
    path('cliente/up/<int:id>', atualizarCliente, name="update.cliente"),
    path('cliente/del/<int:id>', deletarCliente, name="delete.cliente"),
]