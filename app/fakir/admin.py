from django.contrib import admin
from fakir.models import Klient, Sprzedawca, Faktura, PozycjaFaktury

class KlientAdmin(admin.ModelAdmin):
	list_display = ('Imie', 'Nazwisko', 'nr_pesel')




class PozycjeInline(admin.TabularInline):
    model = PozycjaFaktury
    extra = 3
    
 

class FakturaAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Daty', {'fields': ['data_sprzedazy', 'data_wystawienia'], 'classes': ['collapse', 'open']}),
        (None,  {'fields': ['nabywca']}),
        ('Dane nabywcy', {'fields': ['nabywca_adres', 'nabywca_taxid'], 'classes': ['collapse', 'open']}),
        (None, {'fields': ['sprzedawca']}),
        ('Dane sprzedawcy', {'fields': ['sprzedawca_adres', 'sprzedawca_taxid'], 'classes': ['collapse', 'open']}),
        (None, {'fields': ['is_oplacona', 'is_kosztowa']})
    ]
    list_display = ('numer', 'nabywca', 'sprzedawca', 'data_wystawienia')
    list_filter = ['data_wystawienia']
    inlines = [PozycjeInline]
    autocomplete_fields = ["nabywca", "sprzedawca"]

    def get_fields(self, request, obj=None):
        if not obj:
            return ["data_sprzedazy", "data_wystawienia"]
        return super().get_fields(request, obj)
        
class SprzedawcaAdmin(admin.ModelAdmin):
    list_display = ('Sprzedawca_nazwa', 'Sprzedawca_podatek',)
    search_fields = ("Sprzedawca_nazwa", "Sprzedawca_podatek")
    
class PozycjaFakturyAdmin(admin.ModelAdmin):
    list_display = ('nazwa', 'faktura', 'podatek',)

admin.site.register(Klient, KlientAdmin)
admin.site.register(Faktura, FakturaAdmin)
admin.site.register(Sprzedawca, SprzedawcaAdmin)
admin.site.register(PozycjaFaktury, PozycjaFakturyAdmin)
