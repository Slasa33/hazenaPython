from django.shortcuts import render
from django.http import HttpResponse
from HazenaIS.models import Hrac, Zapasy, ZapisZapasu, Udalost, Rozhodci, Klub, Vysledky, Kariera, Sezona
from django.db import connection

def kluby(request):
    k = Klub.objects.filter()
    return render(request, 'kluby.html', {'kluby':k})

def soupiska(request, klub_id):
    k = Kariera.objects.filter(klub=klub_id)
    return render(request, 'hraci_soupiska.html', {'hraci':k})

def zapasy(request):
    z = Zapasy.objects.filter()
    return render(request, 'zapasy.html', {'zapasy':z})


def zapasydetail(request, zapasy_id):
    zdetail = Zapasy.objects.get(id = zapasy_id)
    domacihraci = Kariera.objects.filter(klub=zdetail.domaci) 
    hostehraci = Kariera.objects.filter(klub=zdetail.hoste) 
    sezon = Kariera.objects.filter(klub=zdetail.domaci).first()
    return render(request, 'zapasy_detail.html', {'zapasydetail':zdetail, 'domaci':domacihraci, 'hoste':hostehraci, 'sezona':sezon})