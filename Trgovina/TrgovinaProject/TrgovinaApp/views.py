from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from datetime import date




# Create your views here.

def index(request):
  
    return render(request, 'index.html')


def registration(request):
    User = get_user_model()
    if request.method == "POST":
        ime = request.POST['ime']
        prezime = request.POST['prezime']
        broj_telefona=request.POST['broj_telefona']
        grad=request.POST['grad']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
       
        

        if password == confirm_password:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email je već u upotrebi")
                return redirect('registration')

            else:
                korisnik = User.objects.create_user( email=email, password=password, ime=ime,
                                                    prezime=prezime, broj_telefona=broj_telefona,
                                                    grad=grad)
                korisnik.is_active = True
                korisnik.save()

                return redirect('login')

        else:
            messages.info(request, "Password not the same")
            return redirect('registration')
    else:
        return render(request, 'registration.html')


def login(request):
    if request.method == "POST":

        password = request.POST['password']
        email = request.POST['email']

        korisnik = auth.authenticate(email=email, password=password)

        if korisnik is not None:
            auth.login(request, korisnik)
            return redirect('index')

        else:
            messages.info(request, "Pogresni kredencijali")
            return redirect('login')

    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return render(request, 'index.html')


def search(request):
    query = request.GET.get('q', '')  # Dohvati vrednost parametra 'q' iz URL-a (pretraga)
    proizvodi = Proizvod.objects.filter(naziv_proizvoda__icontains=query)  # Pretraga proizvoda po nazivu
    return render(request, 'search.html', {'proizvodi': proizvodi, 'query': query})



def orders(request):
    narudzbe = Narudzba.objects.filter(korisnik=request.user)
    return render(request, 'orders.html', {'narudzbe': narudzbe})

@login_required
def ordersmake(request):
    if request.method == 'POST':
        grad = request.POST['grad']
        nacin_placanja = request.POST['nacin_placanja']

        narudjba = Narudzba.objects.create(grad=grad, nacin_placanja=nacin_placanja, korisnik=request.user, datum_narudzbe=date.today().isoformat(), detalji_o_isporuci="TBA", ukupna_cijena=0)
        narudjba.save()

    return render(request, 'ordersmake.html')

def orderconfirm(request):
    return render(request, 'orderconfirm.html')

def ordershistory(request):
    narudzbe = Narudzba.objects.filter(korisnik=request.user)
    return render(request, 'ordershistory.html', {'narudzbe': narudzbe})

def products(request):
    proizvodi = Proizvod.objects.all()
    return render(request, 'products.html', {'proizvodi': proizvodi})

def cart(request):
    korpa_korisnika, created = Korpa.objects.get_or_create(korisnik=request.user)
    proizvodi_u_korpi = korpa_korisnika.proizvodi.all()
    
    return render(request, 'cart.html', {'proizvodi_u_korpi': proizvodi_u_korpi})

def dodaj_u_korpu(request, proizvod_id):
    proizvod = get_object_or_404(Proizvod, pk=proizvod_id)
    korpa, created = Korpa.objects.get_or_create(korisnik=request.user)

    # Dodaj proizvod u korpu
    korpa.proizvodi.add(proizvod)

    return redirect('cart') 


def ukloni_iz_korpe(request, proizvod_id):
    proizvod = get_object_or_404(Proizvod, id=proizvod_id)
    korpa_korisnika, created = Korpa.objects.get_or_create(korisnik=request.user)

    if proizvod in korpa_korisnika.proizvodi.all():
        korpa_korisnika.proizvodi.remove(proizvod)

    return redirect('cart')



       
    
    





    


















    



