from django.contrib import admin
from .models import Kunde, Projekt, Mitarbeiter, Aufgabe, Rechnung, Produkt

class KundeAdmin(admin.ModelAdmin):
    list_display = ('name', 'kontakt_email', 'telefonnummer', 'erstellt_am')
    search_fields = ('name', 'kontakt_email')
    list_filter = ('erstellt_am',)

class ProjektAdmin(admin.ModelAdmin):
    list_display = ('titel', 'kunde', 'startdatum', 'enddatum', 'status', 'budget')
    search_fields = ('titel', 'beschreibung')
    list_filter = ('status', 'startdatum', 'enddatum')

class MitarbeiterAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'email', 'eintrittsdatum')
    search_fields = ('name', 'email', 'position')
    list_filter = ('position', 'eintrittsdatum')

class AufgabeAdmin(admin.ModelAdmin):
    list_display = ('titel', 'projekt', 'zugeordnet_an', 'deadline', 'status')
    search_fields = ('titel', 'beschreibung')
    list_filter = ('status', 'deadline')

class RechnungAdmin(admin.ModelAdmin):
    list_display = ('kunde', 'projekt', 'betrag', 'faelligkeitsdatum', 'bezahlt_am')
    search_fields = ('kunde__name', 'projekt__titel')
    list_filter = ('faelligkeitsdatum', 'bezahlt_am')

class ProduktAdmin(admin.ModelAdmin):
    list_display = ('name', 'preis', 'lagerbestand')
    search_fields = ('name', 'beschreibung')
    list_filter = ('name',)

# Registrieren der Modelle mit den erweiterten Admin-Klassen
admin.site.register(Kunde, KundeAdmin)
admin.site.register(Projekt, ProjektAdmin)
admin.site.register(Mitarbeiter, MitarbeiterAdmin)
admin.site.register(Aufgabe, AufgabeAdmin)
admin.site.register(Rechnung, RechnungAdmin)
admin.site.register(Produkt, ProduktAdmin)
