from django.contrib import admin
from .models import Pytanie, Wybor, Grupa, Ankieta




class WyborInline(admin.TabularInline):
    model = Wybor
    extra = 3


class PytanieAdmin(admin.ModelAdmin):
    model = Pytanie
    fieldsets = [
        (None, {'fields': ['pytanie_text', 'pytanie_plik', 'ankieta', 'grupa', 'autor']}),
        ('Informacje o dacie', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    list_display = ('pytanie_text', 'pub_date')
    inlines = [WyborInline]


class GrupaAdmin(admin.ModelAdmin):
    model = Grupa
    fieldsets = [
        (None, {'fields': ['nazwa_grupy', 'ankieta']}),
    ]
    list_display = ('nazwa_grupy',)


class AnkietaAdmin(admin.ModelAdmin):
    model = Ankieta
    fieldsets = [
        (None, {'fields': ['nazwa_ankiety']}),
    ]
    list_display = ('nazwa_ankiety',)




admin.site.register(Pytanie, PytanieAdmin)
admin.site.register(Grupa, GrupaAdmin)
admin.site.register(Ankieta, AnkietaAdmin)
