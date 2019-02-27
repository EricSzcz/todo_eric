from django.test import TestCase
from todo_list.models import Lista
from django.contrib.auth.models import User


class ListaTestCase(TestCase):
    def setUp(self):
        self.usuario = User.objects.create_user(username='João', email='Joao@gmail.com', password='123')
        Lista.objects.create(usuario=self.usuario, item="Testar app", concluido=True)

    """
    Verifica se um item de to-do está sendo criado corretamente
    """
    def test_item_todo(self):

        assert Lista.objects.all().count() == 1
