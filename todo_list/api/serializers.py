from rest_framework.serializers import ModelSerializer
from todo_list.models import Lista


class TodoListSerializer(ModelSerializer):
    class Meta:
        model = Lista
        fields = ('id', 'usuario', 'item', 'concluido')
