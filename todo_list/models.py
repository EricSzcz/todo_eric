from django.db import models
from django.conf import settings

"""
Classe de definição do modelo de dados, da lista de itens do to-do.

usuario   = ID do usuario que está logado no sistema.
item      = Descrição da tarefa a ser realizada.
concluido = Campo booleano que pode ser verdeiro se a tarefa foi concluida ou falso se ainda não. 
"""


class Lista(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item = models.CharField(max_length=200)
    concluido = models.BooleanField(default=False)

    def __str__(self):
        return self.item + '|' + str(self.concluido)
