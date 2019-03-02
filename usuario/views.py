from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.models import User


"""
Classe para logar no sistema.
Metodo GET verifica se o usuário já está logado no sistema, se sim redireciona para a sua lista de to-do
senão direciona para a tela de login

Metodo POST recebe o email do usuáriov consulta no objeto User do django
Cria variável para login com o usuário e senha.
Se variável é válida loga no sistema e redireciona para sua lista de to-do
senão mantem na tela de login e avisa sobre usuário não cadastrado ou senha inválida
"""


class Login(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('lista-todo')
        else:
            return render(request, 'usuario/login.html')

    def post(self, request):
        try:
            usuario_aux = User.objects.get(email=request.POST['email'])
            usuario = authenticate(username=usuario_aux.username, password=request.POST['senha'])

            if usuario is not None:
                login(request, usuario)
                return HttpResponseRedirect('lista-todo')
            else:
                message_senha = True
                return render(request, 'usuario/login.html',
                              {'message_senha': message_senha})

        except User.DoesNotExist:
            message_usuario = True
            return render(request, 'usuario/login.html',
                          {'message_usuario': message_usuario})


"""
Classe para cadastrar novo usuário.
Metodo GET retorna a tela de cadastro.

Metodo POST recebe o email informado e verifica se o mesmo já foi cadastrado no sistema.
Se já existe retorna um aviso para o usuário.
Senão cadastra o novo usuário com dados que foram informados.
Após cadastro já loga no sistema e redireciona para a tela de cadastro dos to-do's
"""


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
            return redirect('lista-todo')

