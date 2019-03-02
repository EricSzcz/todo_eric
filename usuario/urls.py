from django.urls import path

from .views import Login, Cadastro

urlpatterns = [
    path('', Login.as_view(), name='login'),
    path('cadastro/', Cadastro.as_view(), name='cadastro'),

]