from django.db import models
from django.db.models import BooleanField
from django.contrib.auth.models import User


WYBORY = {
    ("Prezydenckie", "Prezydenckie"),
    ("Parlamentarne", "Parlamentarne"),
    ("Starosty roku", "Starosty roku"),
    ("Dziekana wydziału", "Dziekana wydziału"),
}

class Wybory(models.Model):
    rodzaj_wyborow = models.CharField(max_length=30, choices=WYBORY)
    rozpoczecie = models.DateTimeField()
    zakonczenie = models.DateTimeField()

    def __str__(self):
        return 'Wybory ' + self.rodzaj_wyborow

class Kandydat(models.Model):
    imie = models.CharField(max_length=30)
    nazwisko = models.CharField(max_length=30)
    miejscowosc = models.CharField(max_length=30)
    wiek = models.PositiveIntegerField()
    wybory = models.ForeignKey(Wybory, on_delete=models.CASCADE, null=True, blank=True)
    poparcie = models.IntegerField(blank=True, null=True, default=0)

    def __str__(self):
        return self.imie + " " + self.nazwisko

class Wyborca(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    imie = models.CharField(max_length=30, null=True)
    nazwisko = models.CharField(max_length=30, null=True)
    wybory = models.ForeignKey(Wybory, on_delete=models.CASCADE, null=True, blank=True)
    czy_uprawniony = BooleanField(default=False)
    czy_glosowal = BooleanField(default=False)

    def __str__(self):
        return self.imie + " " + self.nazwisko

class Raport(models.Model):
    wybory = models.ForeignKey(Wybory, on_delete=models.CASCADE, null=True, blank=True)
    frekwencja = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.wybory.rodzaj_wyborow

