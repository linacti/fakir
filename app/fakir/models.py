from django.db import models

class Sprzedawca(models.Model):
    nazwa_firmy = models.CharField(max_length=100)
    adres_firmy = models.CharField(max_lenght=100)
    podatek = models.CharField(max_length=20)
    data_zalozenia = models.DateField('Data założenia')
    Telefon_firmy = models.TextField()
    NIP = models..TextField() 
    
 
   
    def __str__(self):
        return self.nazwa
