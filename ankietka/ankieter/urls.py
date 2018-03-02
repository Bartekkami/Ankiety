from django.urls import path
from . import views


app_name= 'ankieter'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pytanie_id>/', views.szczegoly, name='szczegoly'),
    path('<int:pytanie_id>/wyniki/', views.wyniki, name='wyniki'),
    path('<int:pytanie_id>/glos/', views.glos, name='glos'),

]
