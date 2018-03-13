from django.urls import path, re_path
from . import views
from django.conf.urls import url


app_name = 'ankieter'
urlpatterns = [
    re_path(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^signup/$', views.signup_view, name="signup"),
    url(r'^login/$',views.login_view, name="login"),
    url(r'^logout/$', views.logout_view, name="logout"),
    url(r'^create/$', views.create_view, name="create"),
    path('<int:pk>/', views.SzczegolyView.as_view(), name='szczegoly'),
    path('<int:pk>/wyniki/', views.WynikiView.as_view(), name='wyniki'),
    path('<int:pytanie_id>/glos/', views.glos, name='glos'),    

]
