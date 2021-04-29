from django.db import models
from datetime import datetime

# Create your models here.

class Hrac(models.Model):
    jmeno = models.CharField(max_length=50)
    prijmeni = models.CharField(max_length=50)
    rodne_cislo = models.CharField(max_length=25)
    nazev_postu = models.CharField(max_length=25)
    aktivni = models.BooleanField()

    def __str__(self):
        return f"{self.jmeno}, {self.prijmeni}, {self.rodne_cislo}, {self.nazev_postu}, {self.aktivni}"

class Udalost(models.Model):
    nazev_udalosti = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nazev_udalosti}"

class Rozhodci(models.Model):
    jmeno = models.CharField(max_length=50)
    prijmeni = models.CharField(max_length=50)
    rodne_cislo = models.CharField(max_length=25)
    telefon = models.CharField(max_length=25)

    def __str__(self):
        return f"{self.jmeno}, {self.prijmeni}, {self.rodne_cislo}, {self.telefon}"


class Sezona(models.Model):
    nazev_sezony = models.CharField(max_length=25)
    nazev_ligy = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nazev_sezony}, {self.nazev_ligy}"

class Klub(models.Model):
    nazev_klubu = models.CharField(max_length=50)
    prezident_klubu = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    adresa = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nazev_klubu

class Zapasy(models.Model):
    domaci_skore = models.IntegerField()
    hoste_Skore = models.IntegerField()
    datum_cas = models.DateTimeField()
    rozhodci = models.ForeignKey('Rozhodci', on_delete=models.RESTRICT)
    domaci = models.ForeignKey('Klub', on_delete=models.RESTRICT, related_name='domaci_ID')
    hoste = models.ForeignKey('Klub', on_delete=models.RESTRICT, related_name='hoste_ID')

    def __str__(self):
        return f"{self.domaci_skore}, {self.hoste_Skore}, {self.datum_cas}, {self.rozhodci}, {self.domaci}, {self.hoste}"

    def winner(self):
        if self.domaci_skore > self.hoste_Skore:
            return "GREEN"
        elif self.domaci_skore == self.hoste_Skore:
            return "BLACK"
        else:
            return "RED"


class Vysledky(models.Model):
    body = models.IntegerField()
    vyhry = models.IntegerField()
    remizy = models.IntegerField()
    prohry = models.IntegerField()
    vstrelene_branky = models.IntegerField()
    utrzene_branky = models.IntegerField()
    sezona = models.ForeignKey('Sezona', on_delete=models.RESTRICT)
    klub = models.ForeignKey('Klub', on_delete=models.RESTRICT)

    def __str__(self):
        return f"{self.body}, {self.vyhry}, {self.remizy}, {self.prohry}, {self.vstrelene_branky}, {self.utrzene_branky}, {self.sezona}, {self.klub}"

class ZapisZapasu(models.Model):
    cas = models.CharField(max_length=10)
    zapasy = models.ForeignKey('Zapasy', on_delete=models.RESTRICT)
    hrac = models.ForeignKey('Hrac', on_delete=models.RESTRICT)
    udalost = models.ForeignKey('Udalost', on_delete=models.RESTRICT)

    def __str__(self):
        return f"{self.cas}, {self.zapasy}, {self.hrac}, {self.udalost}"

class Kariera(models.Model):
    datum_vstupu = models.DateTimeField(default=datetime.now)
    aktivni = models.BooleanField()
    hrac = models.ForeignKey('Hrac', on_delete=models.RESTRICT)
    klub = models.ForeignKey('Klub', on_delete=models.RESTRICT)
    sezona = models.ForeignKey('Sezona', on_delete=models.RESTRICT)

    def __str__(self):
        return f"{self.datum_vstupu}, {self.aktivni}, {self.hrac}, {self.klub}, {self.sezona}"


    
