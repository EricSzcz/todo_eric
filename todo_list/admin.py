from django.contrib import admin
from .models import Lista

"""
Classe de inclusão de campos na pagina de adminsitrador do Django,
estão sendo atualmente incluidos os campos id, usuario, item e concluido
"""


class ListaAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'item', 'concluido')


admin.site.register(Lista, ListaAdmin)
