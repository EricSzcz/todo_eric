from rest_framework.serializers import ModelSerializer
from todo_list.models import Lista


"""
Classe de Serialização do model da lista de to-dos's.
estão sendo serializados os campos ID, usuario, item e concluido
"""


class TodoListSerializer(ModelSerializer):
    class Meta:
        model = Lista
        fields = ('id', 'usuario', 'item', 'concluido')
