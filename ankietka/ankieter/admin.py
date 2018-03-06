from django.contrib import admin
from .models import Pytanie, Wybor




class WyborInline(admin.TabularInline):
    model = Wybor
    extra = 3


class PytanieAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['pytanie_text', 'pytanie_plik']}),
        ('Informacje o dacie', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    list_display = ('pytanie_text', 'pub_date')
    inlines = [WyborInline]


admin.site.register(Pytanie, PytanieAdmin)
