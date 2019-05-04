from django.urls import path
from .views import *

urlpatterns = [
    path('', listarClientes, name="listar.cliente"),
    path('cliente/novo/', armazenarCliente, name="novo.cliente")
]