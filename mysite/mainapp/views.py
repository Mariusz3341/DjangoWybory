from django.shortcuts import render, redirect, get_object_or_404
from .models import Wybory, Kandydat, Raport, Wyborca
from django.http import HttpResponse
from django.utils import timezone
from django.contrib.auth.decorators import login_required


def home(request):
    all_wybory = Wybory.objects.all()
    return render(request, 'home.html', {'all_wybory': all_wybory})

@login_required(login_url="/admin/login/")
def lista(request, rodzaj_wyborow):
    wybory = get_object_or_404(Wybory, rodzaj_wyborow=rodzaj_wyborow)
    datetime_teraz = timezone.now()
    user = request.user
    wyborca = get_object_or_404(Wyborca, user=user)
    return render(request, 'lista.html', {'rodzaj_wyborow': rodzaj_wyborow, 'wybory': wybory, 'datetime_teraz': datetime_teraz, 'wyborca': wyborca})


def kandydat(request, rodzaj_wyborow, pk):
    kandydat = get_object_or_404(Kandydat, pk=pk)
    return render(request, 'kandydat.html', {'kandydat': kandydat, 'rodzaj_wyborow': rodzaj_wyborow})


def raport(request, rodzaj_wyborow):
    wybory = get_object_or_404(Wybory, rodzaj_wyborow=rodzaj_wyborow)
    raport = get_object_or_404(Raport, wybory=wybory)
    zakonczenie_glosowania = wybory.zakonczenie
    datetime_teraz = timezone.now()

    if request.method == 'POST':
        oddany_glos = wybory.kandydat_set.get(pk=request.POST['glos'])
        wybrany_kandydat = get_object_or_404(Kandydat, pk=oddany_glos.pk)
        user = request.user
        wyborca = get_object_or_404(Wyborca, user=user)
        wybrany_kandydat.poparcie += 1
        wybrany_kandydat.save()
        raport.frekwencja += 1;
        raport.save()
        wyborca.czy_glosowal = True
        wyborca.save()
        return render(request, 'raport.html', {'wybory': wybory, 'zakonczenie_glosowania': zakonczenie_glosowania,
                                           'datetime_teraz': datetime_teraz, 'raport': raport})

    return render(request, 'raport.html', {'wybory': wybory, 'zakonczenie_glosowania': zakonczenie_glosowania,
                                           'datetime_teraz': datetime_teraz, 'raport': raport})
