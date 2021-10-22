from django.db import models
from django.db.models.fields import DecimalField

class Sprzedawca(models.Model):
    nazwa_firmy = models.CharField(max_length=100)
    adres_firmy = models.CharField(max_lenght=100)
    podatek = models.CharField(max_length=20)
    data_zalozenia = models.DateField('Data założenia')
    Telefon_firmy = models.TextField()
    NIP = models..TextField() 
    
 
   
    def __str__(self):
        return self.nazwa
        
class Faktura(models.Model):

    class Meta:
       verbose_name = "Faktura"
       verbose_name_plural = "Faktury"

    numerfaktury = models.CharField(max_length=200, null=True, blank=True,)

    kupujacy = models.ForeignKey(Firma, on_delete=models.SET_NULL, null=True, blank=True, related_name="nabywcy_set")
    
    kupujacy_adres = models.TextField(null=True, blank=True)
    
    kupujacy_podatekid = models.CharField(max_length=20, null=True, blank=True)

    wlasciciel = models.ForeignKey(Firma, on_delete=models.SET_NULL, null=True, blank=True, related_name="sprzedawcy_set")
    
    wlasciciel_adres = models.TextField(null=True, blank=True)
    wlasciciel_podatekid = models.CharField(max_length=20, null=True, blank=True)

    numeracja = models.ForeignKey(NumeracjaFaktur, on_delete=models.SET_NULL, null=True, blank=True)
    
    data_sprzedazy = models.DateField('Data sprzedaży')
    
    data_wystawienia = models.DateField('Data wystawienia')
    
    is_oplacona = models.BooleanField(default=False)
    
    is_kosztowa = models.BooleanField(default=False)

    def __str__(self):
        return self.numer
                
        
class JednostkaMiary(models.Model):
    nazwa = models.CharField(max_length=15)


class Podatek(models.Model):
    nazwa = models.CharField(max_length=15, unique=True)
    stawka = models.DecimalField(max_digits=5, decimal_places=2, default=0, unique=True)


class PozycjaFaktury(models.Model):
    faktura = models.ForeignKey(Faktura, on_delete=models.CASCADE)
    nazwa = models.CharField(max_length=100)
    jednostka_miary = models.ForeignKey(JednostkaMiary, on_delete=models.SET_NULL, null=True, blank=True)
    ilosc = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('1.0'))
    cena = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    wartosc_netto = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    wartosc_all = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    podatek = models.ForeignKey(Podatek, null=True, blank=True, on_delete=models.SET_NULL)
