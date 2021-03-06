from django.urls import path, re_path
from . import views
from django.conf.urls import url


app_name = 'ankieter'
urlpatterns = [
    re_path(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^signup/$', views.signup_view, name="signup"),
    url(r'^login/$',views.login_view, name="login"),
    url(r'^profil/$', views.ProfilView.as_view(), name='profil'),
    url(r'^logout/$', views.logout_view, name="logout"),
    url(r'^create/$', views.dodaj_ankiete, name="create"),
#    url(r'^create2/$', views.dodaj_grupe, name="create2"),
#    url(r'^create3/$', views.dodaj_pytanie, name="create3"),
#    url(r'^create4/$', views.dodaj_wybor, name="create4"),
    url(r'^glownawyniki$', views.Glownawyniki.as_view(), name="glownawyniki"),
    path('<int:pk>/', views.SzczegolyView.as_view(), name='szczegoly'),
    path('<int:pk>/wyniki/', views.WynikiView.as_view(), name='wyniki'),
    path('<int:pytanie_id>/glos/', views.glos, name='glos'),
    path('<int:pk>/grupy/', views.grupy, name='grupy'),
    path('<int:pk>/pytania/', views.pytania, name='pytania'),
    path('<int:pk>/wybory/', views.wybory, name='wybory'),
    path('<int:pk>/create2/', views.dodaj_grupe, name="create2"),
    path('<int:pk>/create3/', views.dodaj_pytanie, name="create3"),
    path('<int:pk>/create4/', views.dodaj_wybor, name="create4"),
]
