from django.shortcuts import render, redirect, get_object_or_404
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


def atualizarCliente(request, id):
    # Se nao achar o objeto retora um 404
    cliente = get_object_or_404(Cliente, pk=id)

    # instancia o form e retorna o cliente e separa o registro
    form = ClienteForm(request.POST or None, request.FILES or None, instance=cliente)
    form2 = ClienteForm(request.POST, request.FILES, instance=cliente)

    if form2.is_valid():
        form2.save()
        return redirect('listar.cliente')

    return render(request, 'update_cliente.html', {'form': form, 'cliente': cliente})

