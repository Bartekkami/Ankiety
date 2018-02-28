from django.shortcuts import render
from django.http import HttpResponse
from .models import Pytanie
from django.template import loader
from django.http import Http404


def index(request):
    lista_ostatnich_pytan = Pytanie.objects.order_by('-pub_date')[:5]
    template = loader.get_template('ankieter/index.html')
    context = {'lista_ostatnich_pytan': lista_ostatnich_pytan,}
    return render(request, 'ankieter/index.html', context)



def szczegoly(request, pytanie_id):
    try:
        pytanie = Pytanie.objects.get(pk=pytanie_id)
    except Pytanie.DoesNotExist:
        raise Http404("Pytanie nie istanieje")
    return render(request, 'ankieter/szczegoly.html', {'Pytanie': pytanie})


def wyniki(request, pytanie_id):
    odpowiedz = "Patrzysz na wyniki pytania %s."
    return HttpResponse(odpowiedz % pytanie_id)

def glos(request, pytanie_id):
    return HttpResponse("glosujesz na pytania %s." % pytanie_id)
