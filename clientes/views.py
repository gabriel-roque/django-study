from django.shortcuts import render
from django.shortcuts import redirect
from .models import Cliente
from .forms import ClienteForm


# Create your views here.
def listarClientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes.html', {'clientes': clientes})


def armazenarCliente(request):
    form = ClienteForm(request.POST, request.FILES, None)

    if form.is_valid():
        form.save()
        return redirect('listar.cliente')

    return render(request, 'novo_cliente.html', {'form': form})
