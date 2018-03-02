from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from .models import Pytanie, Wybor
from django.template import loader
from django.urls import reverse


def index(request):
    lista_ostatnich_pytan = Pytanie.objects.order_by('-pub_date')[:5]
    template = loader.get_template('ankieter/index.html')
    context = {'lista_ostatnich_pytan': lista_ostatnich_pytan,}
    return render(request, 'ankieter/index.html', context)



def szczegoly(request, pytanie_id):
    pytanie = get_object_or_404(Pytanie, pk=pytanie_id)
    return render(request, 'ankieter/szczegoly.html', {'Pytanie': pytanie})


def wyniki(request, pytanie_id):
    odpowiedz = "Patrzysz na wyniki pytania %s."
    return HttpResponse(odpowiedz % pytanie_id)

def glos(request, pytanie_id):
    try:
        zaznaczony_wybor = Pytanie.Wybor_set.get(pk=request.POST['Wybor'])
    except (KeyError, Wybor.DoesNotExist):
        return render(request, 'ankieter/szczgoly.html', {'Pytanie':pytanie, 'error_message' : "Nie odznaczyles wyboru"})
    else:
        zaznaczony_wybor.glosy += 1
        zaznaczony_wybor.save*()
        return HttpResponseRedirect(reverse('ankieter:wyniki', args=(pytanie_id,)))
    return HttpResponse("glosujesz na pytania %s." % pytanie_id)
