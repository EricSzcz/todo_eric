from django.urls import path
from .views import TodoList, NovoTodo, DeletaTodo, EditaTodo, SetarConcluido, SetarNaoConcluido, Sair

urlpatterns = [
    path('', TodoList.as_view(), name="todo-list"),
    path('novo-todo', NovoTodo.as_view(), name="novo-todo"),
    path('deleta-todo/<int:item_id>/', DeletaTodo.as_view(), name="deleta-todo"),
    path('edita-todo/<int:item_id>/', EditaTodo.as_view(), name="edita-todo"),
    path('concluido/<int:item_id>/', SetarConcluido.as_view(), name="conclui-todo"),
    path('nao-concluido/<int:item_id>/', SetarNaoConcluido.as_view(), name="nao-concluido"),
    path('sair/', Sair.as_view(), name="sair"),
    ]
