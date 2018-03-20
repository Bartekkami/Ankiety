from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .models import Pytanie, Wybor, Ankieta, Grupa
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from . import forms
from django.utils import timezone


class IndexView(generic.ListView):
    template_name = 'ankieter/index.html'
    context_object_name = 'lista_ostatnich_ankiet'

    def get_queryset(self):
        return Ankieta.objects.order_by('id') [:15]

class SzczegolyView(generic.DetailView):
    model = Ankieta
    template_name = 'ankieter/szczegoly.html'

class WynikiView(generic.DetailView):
    model = Ankieta
    template_name = 'ankieter/wyniki.html'

def glos(request, pytanie_id,):
    pytanie = Pytanie.objects.get(pk=pytanie_id)
    ankieta = pytanie.ankieta
    if request.method == 'POST':
        wybor_id = request.POST['wybor']
        wybor = Wybor.objects.get(pk=wybor_id)
        wybor.votes += 1
        wybor.save()
        return HttpResponseRedirect(reverse('ankieter:szczegoly', args=(ankieta.id,)))
    return render(request, 'ankieter/szczegoly.html', {'pytanie': pytanie})



def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('ankieter:profil')
    else:
        form = UserCreationForm()
    return render(request,'ankieter/signup.html', {'form':form})



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('ankieter:profil')
    else:
        form = AuthenticationForm()
    return render(request, 'ankieter/login.html', {'form': form})



def logout_view(request):
    if request.method == 'POST':
        logout(request)
    return redirect('ankieter:index')



class Glownawyniki(generic.ListView):
    template_name = 'ankieter/glownawyniki.html'
    context_object_name = 'lista_ostatnich_ankiet'

    def get_queryset(self):
        return Ankieta.objects.order_by('id') [:15]


#@login_required(login_url="/ankieter/login/")
#def create_view(request):
#    if request.method == 'POST':
#        form = forms.StworzAnkiete(request.POST, request.FILES)
#        form2 = forms.StworzGrupe(request.POST, request.FILES)
#        form3 = forms.StworzPytanie(request.POST, request.FILES)
#        form4 = forms.StworzWybor(request.POST, request.FILES)
#        if form.is_valid():
#            instance = form.save(commit=False)
#            instance.autor = request.user
#            instance.save()
#        if form2.is_valid():
#            instance2 = form2.save(commit=False)
#            instance2.ankieta = Ankieta.objects.order_by('id')
#            instance2.save()
#        if form3.is_valid():
#            instance = form3.save(commit=False)
#            instance.autor = request.user
#            instance.pub_date = timezone.now()
#            instance.save()
#        if form4.is_valid():
#            instancja = form4.save(commit=False)
#            instancja.pytanie_id = Pytanie.wybor_id
#            instancja.save()
#            return redirect('ankieter:create')
#    else:
#        form = forms.StworzAnkiete()
#        form2 = forms.StworzGrupe()
#        form3 = forms.StworzPytanie()
#        form4 = forms.StworzWybor()
#    return render(request, 'ankieter/create.html', {'form':form, 'form2':form2, 'form3':form3, 'form4':form4})



class ProfilView(generic.ListView):
    template_name = 'ankieter/profil.html'
    context_object_name = 'lista_ostatnich_ankiet'

    def get_queryset(self):
        return Ankieta.objects.order_by('id') [:15]

@login_required(login_url="/ankieter/login/")
def dodaj_ankiete(request):
    if request.method == 'POST':
        form = forms.StworzAnkiete(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.autor = request.user
            instance.save()
            return redirect('ankieter:create2')
    else:
        form = forms.StworzAnkiete()
    return render(request, 'ankieter/create.html', {'form':form})

@login_required(login_url="/ankieter/login/")
def dodaj_grupe(request):
    if request.method == 'POST':
        form2 = forms.StworzGrupe(request.POST, request.FILES)
        if form2.is_valid():
            instance2 = form2.save(commit=False)
#            instance2.ankieta =
            instance2.save()
            return redirect('ankieter:create3')
    else:
        form2 = forms.StworzGrupe()
    return render(request, 'ankieter/create2.html', {'form2':form2})

@login_required(login_url="/ankieter/login/")
def dodaj_pytanie(request):
    if request.method == 'POST':
        form3 = forms.StworzPytanie(request.POST, request.FILES)
        if form3.is_valid():
            instance3 = form3.save(commit=False)
            instance3.pub_date = timezone.now()
            instance3.autor = request.user
            instance3.save()
            return redirect('ankieter:create4')
    else:
        form3 = forms.StworzPytanie()
    return render(request, 'ankieter/create3.html', {'form3':form3})

@login_required(login_url="/ankieter/login/")
def dodaj_wybor(request):
    if request.method =='POST':
        form4 = forms.StworzWybor(request.POST, request.FILES)
        if form4.is_valid():
            instance4 = form4.save(commit=False)
#            instance4.pytanie_id =
            instance4.save()
            return redirect('ankieter:create4')
    else:
        form4 = forms.StworzWybor()
    return render(request, 'ankieter/create4.html', {'form4':form4})































pass
