from django.contrib import admin
from .models import Klient, Sprzedawca, Faktura, PozycjaFaktury, 


class PozycjaFakturyAdmin(admin.ModelAdmin):
    list_display = ('nazwa', 'faktura', 'podatek',)

admin.site.register(Faktura, FakturaAdmin)
admin.site.register(Sprzedawca, SprzedawcaAdmin)
admin.site.register(PozycjaFaktury, PozycjaFakturyAdmin)
