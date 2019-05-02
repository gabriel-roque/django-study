from django.shortcuts import render
from .models import Cliente


# Create your views here.
def listarClientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes.html', {'clientes': clientes})
