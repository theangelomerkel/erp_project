from django.db import models

# Kundenmodell
class Kunde(models.Model):
    name = models.CharField(max_length=100)
    kontakt_email = models.EmailField()
    telefonnummer = models.CharField(max_length=15, blank=True, null=True)
    adresse = models.TextField(blank=True, null=True)
    erstellt_am = models.DateTimeField(auto_now_add=True)
    bemerkungen = models.TextField(blank=True, null=True)

# Projektmodell
class Projekt(models.Model):
    kunde = models.ForeignKey(Kunde, on_delete=models.CASCADE)
    titel = models.CharField(max_length=200)
    beschreibung = models.TextField()
    startdatum = models.DateField()
    enddatum = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=50, choices=[('in_progress', 'In Progress'), ('completed', 'Completed'), ('pending', 'Pending')])
    budget = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

# Mitarbeitermodell
class Mitarbeiter(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    email = models.EmailField()
    telefonnummer = models.CharField(max_length=15, blank=True, null=True)
    geburtsdatum = models.DateField(blank=True, null=True)
    eintrittsdatum = models.DateField()

# Aufgabenmodell
class Aufgabe(models.Model):
    projekt = models.ForeignKey(Projekt, on_delete=models.CASCADE)
    titel = models.CharField(max_length=200)
    beschreibung = models.TextField()
    zugeordnet_an = models.ForeignKey(Mitarbeiter, on_delete=models.SET_NULL, blank=True, null=True)
    deadline = models.DateField()
    status = models.CharField(max_length=50, choices=[('to_do', 'To Do'), ('in_progress', 'In Progress'), ('done', 'Done')])

# Rechnungsmodell
class Rechnung(models.Model):
    kunde = models.ForeignKey(Kunde, on_delete=models.CASCADE)
    projekt = models.ForeignKey(Projekt, on_delete=models.SET_NULL, blank=True, null=True)
    betrag = models.DecimalField(max_digits=10, decimal_places=2)
    faelligkeitsdatum = models.DateField()
    bezahlt_am = models.DateField(blank=True, null=True)
    bemerkungen = models.TextField(blank=True, null=True)

# Lagermodell
class Produkt(models.Model):
    name = models.CharField(max_length=100)
    beschreibung = models.TextField()
    preis = models.DecimalField(max_digits=10, decimal_places=2)
    lagerbestand = models.IntegerField()
