#from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.viewsets import ModelViewSet
from todo_list.models import Lista
from .serializers import TodoListSerializer


class UserViewSet(ModelViewSet):
    serializer_class = TodoListSerializer

    def get_queryset(self):
        usuario = self.request.user
        return Lista.objects.filter(usuario=usuario)

