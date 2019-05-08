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
    # Recebe o id localizar o objeto
    cliente = Cliente.objects.get(id=id)

    # instancia o form e retorna o cliente e separa o registro
    form = ClienteForm(request.POST or None, request.FILES or None, instance=cliente)

    # inicalizando variavel para ser um dicionário
    data = {'form': form, 'cliente': cliente}

    if form.is_valid():
        form.save()
        return redirect('listar.cliente')
    return render(request, 'update_cliente.html', data)


def deletarCliente(request, id):
    Cliente.objects.get(id=id).delete()

    return redirect('listar.cliente')
