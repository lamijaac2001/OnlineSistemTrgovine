from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from datetime import datetime
from django.utils.crypto import get_random_string
from datetime import timedelta
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Manager(BaseUserManager):

    def create_superuser(self, email, password, ime, prezime, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        return self.create_user(email, password, ime, prezime, **other_fields)

    def create_user(self, email, password, ime, prezime, **other_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, ime=ime, prezime=prezime, **other_fields)
        user.set_password(password)
        user.save()
        return user


class MyUser(AbstractBaseUser, PermissionsMixin):

    password = models.CharField(max_length=250)
    email = models.EmailField(max_length=80, unique=True)

    ime = models.CharField(max_length=30)
    prezime = models.CharField(max_length=30)
    broj_telefona = models.CharField(max_length=15, blank=True)
    grad=models.CharField(max_length=30)

    date_of_registration = models.DateField(blank=True, null=True)
    
    AKTIVAN = 'A'
    NEAKTIVAN = 'N'
    BLOKIRAN='B'

    Status = [
        (AKTIVAN, 'Aktivan'),
        (NEAKTIVAN, 'Neaktivan'),
        (BLOKIRAN, 'Blokiran'),
    ]

    Status = models.CharField(max_length=1, choices=Status, default=AKTIVAN,)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = Manager()

    USERNAME_FIELD = 'email' # prijava korisnika

    REQUIRED_FIELDS = ['ime', 'prezime'] # dodajemo atribute koji nisu nullable tj elemente pri registraciji

    def __str__(self):
        return self.ime + self.prezime
    

class Narudzba(models.Model):
    datum_narudzbe=models.DateField(blank=True, null=True)
    
    ukupna_cijena = models.DecimalField(max_digits=10, decimal_places=2)
    grad = models.CharField(max_length=30)
    korisnik = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    nacin_placanja=models.CharField(max_length=30)
    detalji_o_isporuci=models.CharField(max_length=255)
    placeno = models.BooleanField(default=False)

    U_OBRADI = 'U'
    POSLANO = 'P'
    ISPORUCENO='I'
    OTKAZANO='O'

    Status = [
        (U_OBRADI, 'U'),
        (POSLANO, 'P'),
         (ISPORUCENO, 'I'),
        (OTKAZANO, 'O'),
    ]

    status = models.CharField(max_length=1, choices=Status, default=POSLANO,)

class Proizvod(models.Model):
        naziv_proizvoda=models.CharField(max_length=30)
        opis=models.CharField(max_length=255)
        količina=models.IntegerField(default=1)
        cijena=models.DecimalField(max_digits=10,decimal_places=2)
        brend=models.CharField(max_length=30)
        boja=models.CharField(max_length=10)
        veličina=models.IntegerField(default=10)
        datum_dodavanja=models.DateField(blank=True, null=True)
        grad=models.CharField(max_length=30)

class Korpa(models.Model):

    korisnik = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    proizvodi = models.ManyToManyField(Proizvod)
    ukupna_cijena=models.DecimalField(max_digits=10,decimal_places=2)

class Placanje(models.Model):
     tip_placanja=models.CharField(max_length=10)
     broj_kartice=models.CharField(max_length=30)
     ime_nosioca_kartice=models.CharField(max_length=30)
     datum_isteka=models.DateField(blank=True, null=True)
     ukupan_iznos=models.DecimalField(max_digits=10,decimal_places=2)
     narudzba = models.ForeignKey(Narudzba, on_delete=models.CASCADE)

class Recenzija(models.Model):
     tekst_recenzije=models.CharField(max_length=255)
     ocjena=models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
     datum_postavke=models.DateField(blank=True, null=True)
     korisnik = models.ForeignKey(MyUser, on_delete=models.CASCADE)
     proizvod = models.ForeignKey(Proizvod, on_delete=models.CASCADE)

class Kategorija(models.Model):
     naziv_kategorije=models.CharField(max_length=30)
     opis_kategorije=models.CharField(max_length=255)





