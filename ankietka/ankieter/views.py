from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .models import Pytanie, Wybor
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from . import forms


class IndexView(generic.ListView):
    template_name = 'ankieter/index.html'
    context_object_name = 'lista_ostatnich_pytan'

    def get_queryset(self):
        return Pytanie.objects.order_by('-pub_date') [:15]

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

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            #zaloguj i redirect na profil usera
            login(request, user)
            return redirect('ankieter:index')
    else:
        form = UserCreationForm()
    return render(request,'ankieter/signup.html', {'form':form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            #zaloguj i redirect na profil usera
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('ankieter:index')
    else:
        form = AuthenticationForm()
    return render(request, 'ankieter/login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
    return redirect('ankieter:index')


@login_required(login_url="/ankieter/login/")
def create_view(request):
    if request.method == 'POST':
        form = forms.StworzAnkiete(request.POST, request.FILES)
        if form.is_valid():
            return redirect('ankieter:index')
    else:
        form = forms.StworzAnkiete()
    return render(request, 'ankieter/create.html', {'form': form})








































pass
