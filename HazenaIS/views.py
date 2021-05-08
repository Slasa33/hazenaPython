from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from HazenaIS.models import Hrac, Zapasy, ZapisZapasu, Udalost, Rozhodci, Klub, Vysledky, Kariera, Sezona
from django.db import connection
from HazenaIS.forms import ZapasSearchForm, HracForm, KlubForm, ZapasyForm, KarieraForm, HracAddForm, HracSearchForm, KarieraDeleteForm
from django.db.models import Q
from django.http import HttpResponseRedirect
from datetime import datetime

def kluby(request):
    k = Klub.objects.filter()
    return render(request, 'kluby.html', {'kluby':k})

def soupiska(request, klub_id):
    k = Kariera.objects.filter(klub=klub_id, aktivni=True)
    return render(request, 'hraci_soupiska.html', {'hraci':k})

def zapasy(request):
    if request.method == 'POST':
        form = ZapasSearchForm(request.POST)
        if form.is_valid():
            searched = form.cleaned_data['searched_name']
            z = Zapasy.objects.filter(Q(domaci__nazev_klubu__contains=searched) | Q(hoste__nazev_klubu__contains=searched))
        else:
            z = Zapasy.objects.all()
    else:
        form = ZapasSearchForm()
        z = Zapasy.objects.all()
    return render(request, 'zapasy.html', {'zapasy':z, 'form':form})


def zapasydetail(request, zapasy_id):
    zdetail = Zapasy.objects.get(id = zapasy_id)
    domacihraci = Kariera.objects.filter(klub=zdetail.domaci) 
    hostehraci = Kariera.objects.filter(klub=zdetail.hoste) 
    sezon = Kariera.objects.filter(klub=zdetail.domaci).first()
    return render(request, 'zapasy_detail.html', {'zapasydetail':zdetail, 'domaci':domacihraci, 'hoste':hostehraci, 'sezona':sezon})

def hrac_edit(request, hrac_id):
    try:
        h = Hrac.objects.get(id = hrac_id)
    except Hrac.DoesNotExist:
        raise Http404("Hrac nenalezen")
    if request.method == 'POST':
        form = HracForm(request.POST, instance = h)
        if form.is_valid():
            form.save()
            Hrac.objects.filter(id = hrac_id).update(aktivni = True)
            return redirect('kluby')
    else:
        form = HracForm(instance = h)
    return render(request, 'hrac_edit.html', {'form':form})


def klub_add(request):
    if request.method == 'POST':
        form = KlubForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('kluby')
    else:
        form = KlubForm()
    return render(request, 'kluby_add.html', {'form':form})

def zapasy_add(request):
    if request.method == 'POST':
        form = ZapasyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('zapasy')
    else:
        form = ZapasyForm()
    return render(request, 'zapasy_add.html', {'form':form})

def tabulka(request):
    t = Vysledky.objects.all()
    return render(request, 'tabulka.html', {'tabulka':t})

def hraci(request):
    if request.method == 'POST':
        form = HracSearchForm(request.POST)
        if form.is_valid():
            searched = form.cleaned_data['searched_hrac']
            h = Hrac.objects.filter(nazev_postu = searched, aktivni=False)
        else:
            h = Hrac.objects.all()
    else:
        form = HracSearchForm()
        h = Hrac.objects.filter(aktivni=False)

    return render(request, 'hraci.html', {'hraci':h, 'form':form})

def hraci_add(request):
    if request.method == 'POST':
        form = HracAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hraci')
    else:
        form = HracAddForm()
    return render(request, 'hraci_add.html', {'form':form})

def kariera(request):
    if request.method == 'POST':
        form = KarieraForm(request.POST)
        if form.is_valid():
            hracid = form.cleaned_data['hrac']
            Hrac.objects.filter(id = hracid.id).update(aktivni = True)
            form.save()
            Kariera.objects.filter(hrac = hracid.id).update(aktivni = True)
            return redirect('hraci')
    else:
        form = KarieraForm()
        form.fields["hrac"].queryset = Hrac.objects.filter(aktivni = False)
    return render(request, 'kariera.html', {'form':form})

def rozhodci(request):
    r = Rozhodci.objects.all()
    return render(request, 'rozhodci.html', {'rozhodci':r})


def end_kariera(request, hrac_id):
    k = Hrac.objects.get(id = hrac_id)
    a = Kariera.objects.get(hrac = k.id)

    if request.method == 'POST':
        form = KarieraDeleteForm(request.POST, instance = a)
        if form.is_valid():
            form.save()
            Kariera.objects.filter(hrac = k.id).delete()
            Hrac.objects.filter(id = k.id).update(aktivni = False)
            return redirect('kluby')
    else:
        form = KarieraDeleteForm(instance = a)

    return render(request, 'kariera_delete.html', {'form':form, 'hrac':k})
