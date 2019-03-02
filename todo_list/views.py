from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.shortcuts import render, redirect

from .models import Lista
from .forms import ListaForm


"""
Classe para retornar a lista de to-do's do usuário.
Para retornar somente os todos do usuário corrente está sendo usado
um filter na consulta dos objetos do model,
classe criada usando o conceito de Class-based view
"""


class ListaTodo(
        LoginRequiredMixin, View):
    def get(self,
            request):
        usuario = request.user
        itens = Lista.objects.filter(usuario=usuario)
        return render(request, 'lista-todo/lista-todo.html', {'itens': itens})


"""
Classe para criar um novo to-do.
Metodo POST recebe as informações da request e passa para o form.
É feita a verifição do form, caso seja válido as informações serão
salvas senão será retornado um aviso para o usuário
"""


class NovoTodo(
        LoginRequiredMixin, View):
    def post(self,
             request):
        form = ListaForm(request.POST or None, user=request.user)

        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            messages.success(request, ('Item adicionado com sucesso'))
            return redirect('lista-todo')
        else:
            messages.success(request, ('Ouve um erro ao tentar'
                                       ' adicionar o item'))
            return redirect('lista-todo')


"""
Classe para deletar o item da lista caso o usuário não o queira mais.
Metodo recebe o ID do item consulta no model e deleta o mesmo.
"""


class DeletaTodo(
        LoginRequiredMixin, View):
    def get(self,
            request,
            item_id):
        item = Lista.objects.get(id=item_id)
        item.delete()
        return redirect('lista-todo')


"""
Classe para editar a descrição de um item.
Metodo GET recebe o ID do item e direciona o usuário para a página
de edição.
Metodo POST válida o form após edição e salva o mesmo .
"""


class EditaTodo(
        LoginRequiredMixin, View):
    def get(self,
            request,
            item_id):
        item = Lista.objects.get(id=item_id)

        return render(request, 'lista-todo/edita-todo.html', {'item': item})

    def post(self,
             request,
             item_id):
        item = Lista.objects.get(id=item_id)
        form = ListaForm(request.POST or None,
                         instance=item, user=request.user)

        if form.is_valid():
            form.save()
        return redirect('lista-todo')


"""
Classe para setar o status do to-do para concluído.
Metodo GET recebe o ID do item e seta concluído como True e retorna
a lista de itens novamente.
"""


class SetarConcluido(
        LoginRequiredMixin, View):
    def get(self,
            request,
            item_id):
        item = Lista.objects.get(id=item_id)
        item.concluido = True
        item.save()
        return redirect('lista-todo')


"""
Classe para setar o status do to-do para não concluído.
Metodo GET recebe o ID do item e seta concluÍdo como False e retorna
a lista de itens novamente.
"""


class SetarNaoConcluido(
        LoginRequiredMixin, View):
    def get(self,
            request,
            item_id):
        item = Lista.objects.get(id=item_id)
        item.concluido = False
        item.save()
        return redirect('lista-todo')


"""
Classe para deslogar o usuário corrente.
Metodo GET recebe o request e passa para o metodo logout do Django.
Após isto redireciona para a página de login.
"""


class Sair(
        LoginRequiredMixin, View):
    def get(self,
            request):
        logout(request)
        return HttpResponseRedirect('/')
