from django import forms
from .models import Lista


"""
Classe de definição do form da lista de to-do's.

No primeiro metodo foi definido o construtor da classe para incluír o usuário logado no sistema no form.

O segundo metodo salva a instância do form com os dados que foram informados pelo usuário e seu ID de usuário,
desta forma não é necessário incluír um campo de usuário no formulario para depois ser coletado, evitando assim
que algum usuário mal intencionado possa inspecionar os elementos da página e trocar o ID do usuário salvando
informações na to-do list de outro usuário.

Por último uma classe Meta para enviar os campos do model para o form.
"""


class ListaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self._user = kwargs.pop('user')
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.usuario = self._user
        if commit:
            instance.save()
        return instance

    class Meta:
        model = Lista
        fields = ["item", "concluido"]
