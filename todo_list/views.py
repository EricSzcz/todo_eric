from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Lista
from .forms import ListaForm
from django.contrib import messages


class TodoList(LoginRequiredMixin, View):
    def get(self, request):
        usuario = request.user
        itens = Lista.objects.filter(usuario=usuario)
        return render(request, 'todo_list/todo_list.html', {'itens': itens})

    def post(self, request):
        pass


class NovoTodo(LoginRequiredMixin, View):
    def get(self, request):
        pass

    def post(self, request):
        form = ListaForm(request.POST or None, user=request.user)

        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            messages.success(request, ('Item adicionado com sucesso'))
            return redirect('todo-list')
        else:
            return HttpResponse(str(form.errors))


class DeletaTodo(LoginRequiredMixin, View):
    def get(self, request, item_id):
        item = Lista.objects.get(id=item_id)
        item.delete()
        return redirect('todo-list')


class EditaTodo(LoginRequiredMixin, View):
    def get(self, request, item_id):
        item = Lista.objects.get(id=item_id)

        return render(request, 'todo_list/edita-todo.html', {'item': item})

    def post(self, request, item_id):
        item = Lista.objects.get(id=item_id)
        form = ListaForm(request.POST or None, instance=item)

        if form.is_valid():
            form.save()
        return redirect('todo-list')


class SetarConcluido(LoginRequiredMixin, View):
    def get(self, request, item_id):
        item = Lista.objects.get(id=item_id)
        item.concluido = True
        item.save()
        return redirect('todo-list')


class SetarNaoConcluido(LoginRequiredMixin, View):
    def get(self, request, item_id):
        item = Lista.objects.get(id=item_id)
        item.concluido = False
        item.save()
        return redirect('todo-list')


class Sair(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')
