from django.shortcuts import render
from django.contrib.auth import login, authienticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect

def singup(request):
    if request.method == 'POST'
    form = UserCreationForm(request.POST)
    if form.is_valid():
       form.save()
       username + form.cleaned_data.get('username')
       raw_password = form.cleaned_data.get('password1')
       user = authenticate(username=username, password=raw_password)
       login(request, user)
    else:
       form = UserCreationForm()
    return render(request, 'singup.html', {'form': form})

