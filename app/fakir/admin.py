from django.contrib import admin
from .models import Klient, Sprzedawca, Faktura, PozycjaFaktury, 

class PozycjeInline(admin.TabularInline):
    model = PozycjaFaktury
    extra = 3


class SprzedawcaAdmin(admin.ModelAdmin):
    list_display = ('Sprzedawca_nazwa', 'Sprzedawca_podatek',)
    search_fields = ("Sprzedawca_nazwa", "Sprzedawca_podatek")
    
class PozycjaFakturyAdmin(admin.ModelAdmin):
    list_display = ('nazwa', 'faktura', 'podatek',)

admin.site.register(Faktura, FakturaAdmin)
admin.site.register(Sprzedawca, SprzedawcaAdmin)
admin.site.register(PozycjaFaktury, PozycjaFakturyAdmin)
