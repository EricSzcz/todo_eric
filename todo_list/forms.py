from django import forms
from .models import Lista


"""
Classe de definição do form da lista de to-do's.

No primeiro metodo foi definido construtor da classe para incluir o usuario logado no sistema no form.

O segundo metodo salva a instancia do form com od dados que foram informados pelo usuario e seu ID de usuario,
desta forma não é necessario incluir um campo de usuario no formulario para depois ser coletado, evitando assim
que algum usuario mal intencionado possa inspecionar os elementos da pagina e trocar o ID do usuario salvando
informações em outros usuarios.

Por ultimo uma classe Meta para enviar os campos do model para o form.
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
