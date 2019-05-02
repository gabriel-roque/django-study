from django.shortcuts import render


# Create your views here.


def lerBanco(nome):
    lista = [
        {'nome': 'gabriel', 'idade': 20},
        {'nome': 'camila', 'idade': 15},
        {'nome': 'eduarda', 'idade': 17}
    ]

    for pessoa in lista:
        if pessoa['nome'] == nome:
            return pessoa
    else:
        return {'nome': 'Nao encontrado'}


def indexCliente(request, nome):
    registro = lerBanco(nome)

    return render(request, 'pessoa.html', {'nome': registro['nome']})
