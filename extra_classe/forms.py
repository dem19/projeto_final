from django.forms import ModelForm
from .models import *

class Horariodisponivel(ModelForm):
    class Meta:
        model = Professor
        fields = ['nome_professor','disciplina','data', 'hora']


class Horariomarcado(ModelForm):
    class Meta:
        model = Atendimento
        fields = ['nome_professor','disciplina','data', 'hora']


class Alunofazercomentario(ModelForm):
    class Meta:
        model = Comentario
        fields = ['nome_aluno','disciplina','duvidas']

class Alunodisponivelizar(ModelForm):
    class Meta:
        model = Aluno
        fields = ['disciplina','nome','Confirmar']
