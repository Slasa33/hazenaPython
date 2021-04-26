from django.shortcuts import render
from django.http import HttpResponse
from HazenaIS.models import Hrac, Zapasy, ZapisZapasu, Udalost, Rozhodci, Klub, Vysledky, Kariera, Sezona
from django.db import connection

def hello(request):
    return HttpResponse("<h1>Hello World</h1>")

def klub_info(request, klub_id):
    k = Klub.objects.get(id = klub_id)
    return render(request, 'klub_info.html',{'klub':k})


def kluby(request):
    k = Klub.objects.filter()
    return render(request, 'kluby.html', {'kluby':k})


def soupiska(request, klub_id):
    k = Kariera.objects.filter(klub=klub_id)
    return render(request, 'hraci_soupiska.html', {'hraci':k})