from django.forms import ModelForm
from .models import Cliente


class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['pri_nome', 'seg_nome', 'idade', 'salario', 'bio', 'photo']

# ModelForm uma classe do Django que ja faz as validacoes e cria os formularios
