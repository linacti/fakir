from django.db import models
from django.db.models.fields import DecimalField

class Klient(models.Model):
    Imie = models.CharField(max_length=100)
    Nazwisko = models.CharField(max_length=100)
    nr_pesel = models.TextField(max_length=11)
    Adres = models.CharField(max_lenght=150)
    kod_pocztowy = models.TextField(max_length=6)
    miasto = models.CharField(max_length=50)
    data_urodzenia = models.DateField()
    nr_telefonu = models.TextField(max_length=9)
    
    def __str__(self):
        return self.nazwa

class Sprzedawca(models.Model):
    
    Sprzedawca_nazwa = models.CharField(max_length=100)
    
    Sprzedawca_adres = models.CharField(max_lenght=100)
    
    Sprzedawca_podatek = models.CharField(max_length=20)
    
    Sprzedawca_data_zalozenia = models.DateField('Data założenia')
    
    Sprzedawca_telefon = models.TextField()
    
    Sprzedawca_NIP = models.TextField() 
    
    Sprzedawca_wlasciciel = models.TextField()
    
    class Meta:
        verbose_name = "Firma"
        
        verbose_name_plural = "Sprzedawcy"
    def __str__(self):
        return self.nazwa
        
class Faktura(models.Model):

    class Meta:
        verbose_name = "Faktura"
        verbose_name_plural = "Faktury"

    numer = models.CharField(max_length=200, null=True, blank=True,)

    nabywca = models.ForeignKey(Firma, on_delete=models.SET_NULL, null=True, blank=True, related_name="nabywcy_set")
    nabywca_taxid = models.CharField(max_length=20, null=True, blank=True)
    nabywca_adres = models.TextField(null=True, blank=True)


    sprzedawca = models.ForeignKey(Firma, on_delete=models.SET_NULL, null=True, blank=True, related_name="sprzedawcy_set")
     sprzedawca_taxid = models.CharField(max_length=20, null=True, blank=True)
    sprzedawca_adres = models.TextField(null=True, blank=True)
  
  
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
