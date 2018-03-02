from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from .models import Pytanie, Wybor
from django.template import loader
from django.urls import reverse
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'ankieter/index.html'
    context_object_name = 'lista_ostatnich_pytan'

    def get_queryset(self):
        return Pytanie.objects.order_by('-pub_date') [:5]

class SzczegolyView(generic.DetailView):
    model = Pytanie
    template_name = 'ankieter/szczegoly.html'

class WynikiView(generic.DetailView):
    model = Pytanie
    template_name = 'ankieter/wyniki.html'



def glos(request, pytanie_id):
    pytanie = Pytanie.objects.get(pk=pytanie_id)
    if request.method == 'POST':
        wybor_id = request.POST['wybor']
        wybor = Wybor.objects.get(pk=wybor_id)
        wybor.votes += 1
        wybor.save()
        return HttpResponseRedirect(reverse('ankieter:wyniki', args=(pytanie_id,)))
    return render(request, 'ankieter/szczgoly.html', {'pytanie': pytanie})

    # return HttpResponse("glosujesz na pytanie: %s" % pytanie)
    # Wybor.objects.get(pk=)
    # try:
    #     zaznaczony_wybor = Pytanie.wybor_set.get(pk=request.POST['Wybor'])
    # except (KeyError, Wybor.DoesNotExist):
    #     return render(request, 'ankieter/szczgoly.html', {'Pytanie':pytanie, 'error_message' : "Nie odznaczyles wyboru"})
    # else:
    #     zaznaczony_wybor.glosy += 1
    #     zaznaczony_wybor.save*()
    #     return HttpResponseRedirect(reverse('ankieter:wyniki', args=(pytanie_id,)))
    # return HttpResponse("glosujesz na pytania %s." % pytanie_id)
