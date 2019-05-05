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

    if form.is_valid():
        form.save()
        return redirect('listar.cliente')

    return render(request, 'update_cliente.html', {'form': form, 'cliente': cliente})


def deletarCliente(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    # form = ClienteForm(request.POST, request.FILES, instance=cliente)

    if request.method == 'POST':
        cliente.delete()
        return redirect('listar.cliente')


