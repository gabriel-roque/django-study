from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return render(request, 'index.html')


def indexCliente(request, nome):
    registro = lerBanco(nome)

    return render(request, 'pessoa.html', {'nome': registro['nome']})


def artigos(request, year):
    return HttpResponse('O ano enviado foi: ' + str(year))


def rota(request, nome):
    return HttpResponse('Rota com nome de ' + nome)


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


def buscarPessoa(request, nome):
    return HttpResponse('Resultado de Busca: ' + lerBanco(nome)['nome'])
