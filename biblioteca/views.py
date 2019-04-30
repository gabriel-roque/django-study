from django.http import HttpResponse


def hello(request):
    return HttpResponse('Hello World')


def artigos(request, year):
    return HttpResponse('O ano enviado foi: ' + str(year))


def rota(request, nome):
    return HttpResponse('Rota com nome de ' + nome)


