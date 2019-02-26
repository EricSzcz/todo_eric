from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.models import User


class Login(View):
    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect('todo-list')
        else:
            return render(request, 'usuario/login.html')

    def post(self, request):
        usuario_aux = User.objects.get(email=request.POST['email'])
        usuario = authenticate(username=usuario_aux.username, password=request.POST['senha'])

        if usuario is not None:
            login(request, usuario)
            return HttpResponseRedirect('todo-list')

        return HttpResponseRedirect('/')



class Cadastro(View):
    def get(self, request):
        return render(request, 'usuario/cadastro.html')

    def post(self, request):
        try:
            usuario_aux = User.objects.get(email=request.POST['email'])

            if usuario_aux:
                return render(request, 'usuario/cadastro.html', {'msg': 'Usuario ja existe'})

        except User.DoesNotExist:
            nome_usuario = request.POST['nome-usuario']
            email = request.POST['email']
            senha = request.POST['senha']

            novoUsuario = User.objects.create_user(username=nome_usuario, email=email, password=senha)
            novoUsuario.save()

            usuario = authenticate(username=nome_usuario, password=senha)

            login(request, usuario)
            return redirect('todo-list')

