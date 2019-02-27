from rest_framework.viewsets import ModelViewSet
from todo_list.models import Lista
from .serializers import TodoListSerializer


"""
Classe para responder as requisições dos endpoints da API
Recebe a classe de serialização.
Sobreescreve o Metodo GET para retornar somente os dados respectivos do usuário que fez a requisição. 
"""


class UserViewSet(ModelViewSet):
    serializer_class = TodoListSerializer

    def get_queryset(self):
        usuario = self.request.user
        return Lista.objects.filter(usuario=usuario)

