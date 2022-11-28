from django.http import HttpResponse


def teste(request):
    return HttpResponse("Olá mundo do django")


def teste2(request):
    return HttpResponse("Outra aba aqui ó")
