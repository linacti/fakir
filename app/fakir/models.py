from django.db import models
from django.db.models.fields import DecimalField
from django.core.validators import RegexValidator

class Klient(models.Model):
    Imie = models.CharField(max_length=100)
    Nazwisko = models.CharField(max_length=100)
    pesel = RegexValidator(regex=r'^\+?1?\d{11,11}$', message="pesel musi miec 11 liter")
    nr_pesel = models.CharField(validators=[pesel], max_length=11, blank=True) 
    Adres = models.CharField(max_length=150)
    kod_pocztowy = models.CharField(max_length=6)
    Adres = models.CharField(max_length=150)
    miasto = models.CharField(max_length=50)
    data_urodzenia = models.DateField()
    nr_telefonu = models.IntegerField()
    

class Sprzedawca(models.Model):
    
    Sprzedawca_nazwa = models.CharField(max_length=100)
    
    Sprzedawca_adres = models.CharField(max_length=100)
    
    Sprzedawca_podatek = models.IntegerField()
    
    Sprzedawca_data_zalozenia = models.DateField('Data założenia')
    
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    Sprzedawca_numer = models.CharField(validators=[phone_regex], max_length=17, blank=True) 
    
    
    nip = RegexValidator(regex=r'^\+?1?\d{10,10}$', message="Nip must have 10 digits")
    Sprzedawca_NIP = models.CharField(validators=[nip], max_length=10, blank=True)

    class Meta:
        verbose_name = "Firma"
        
        verbose_name_plural = "Sprzedawcy"
    def __str__(self):
        return self.Sprzedawca_nazwa
        
class Faktura(models.Model):

    class Meta:
        verbose_name = "Faktura"
        verbose_name_plural = "Faktury"

    numer = models.CharField(max_length=200, null=True, blank=True,)

    nabywca = models.ForeignKey(Sprzedawca, on_delete=models.SET_NULL, null=True, blank=True, related_name="nabywcy_set")
    nabywca_taxid = models.CharField(max_length=20, null=True, blank=True)
    nabywca_adres = models.TextField(null=True, blank=True)


    sprzedawca = models.ForeignKey(Sprzedawca, on_delete=models.SET_NULL, null=True, blank=True, related_name="sprzedawcy_set")
    sprzedawca_taxid = models.TextField(null=True, blank=True)
    sprzedawca_adres = models.TextField(null=True, blank=True)
    
    data_sprzedazy = models.DateField('Data sprzedaży')
    data_wystawienia = models.DateField('Data wystawienia')
    is_oplacona = models.BooleanField(default=False)
    is_kosztowa = models.BooleanField(default=False)
  
  
  
        
class JednostkaMiary(models.Model):
    nazwa = models.CharField(max_length=15)


class Podatek(models.Model):
    nazwa = models.CharField(max_length=15, unique=True)
    stawka = models.DecimalField(max_digits=5, decimal_places=2, default=0, unique=True)


class PozycjaFaktury(models.Model):
    faktura = models.ForeignKey(Faktura, on_delete=models.CASCADE)
    nazwa = models.CharField(max_length=100)
    jednostka_miary = models.ForeignKey(JednostkaMiary, on_delete=models.SET_NULL, null=True, blank=True)
    
    cena = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    wartosc_netto = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    wartosc_all = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    podatek = models.ForeignKey(Podatek, null=True, blank=True, on_delete=models.SET_NULL)
