from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return render(request, 'index.html')


def artigos(request, year):
    return HttpResponse('O ano enviado foi: ' + str(year))


def rota(request, nome):
    return HttpResponse('Rota com nome de ' + nome)


def lerBanco(nome):
    lista = [
        {'nome': 'gabriel'},
        {'nome': 'camila'},
        {'nome': 'eduarda'}
    ]

    for pessoa in lista:
        if pessoa['nome'] == nome:
            return pessoa
    else:
        return {'nome': 'Nao encontrado'}


def buscarPessoa(request, nome):
    return HttpResponse('Resultado de Busca: ' + lerBanco(nome)['nome'])
