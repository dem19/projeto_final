from django.shortcuts import render, redirect
from .forms import *
from .models import Professor
from django.contrib.auth.decorators import login_required


def home(request):
    horario = Atendimento.objects.all()
    return render(request, 'home.html', {'horario': horario})


@login_required
def professor(request):
    hora = Professor.objects.all()
    return render(request, 'professor.html', {'hora': hora})


@login_required
def salvar(request, id):
    marcar = Professor.objects.get(id=id)
    horas = Horariomarcado(request.POST or None, instance=marcar)
    hor = Horariomarcado(request.POST or None)
    if horas.is_valid():
        hor.save()
        horas.save()
        return redirect(home)

    return render(request, 'salvar.html', {'horas': horas})


@login_required
def mostrar(request):
    horario = Atendimento.objects.all()
    return render(request, 'disponibilidade.html', {'horario': horario})


@login_required
def apaga(request, id):
    cadastrado = Atendimento.objects.get(id=id)
    if request.method == 'POST':
        cadastrado.delete()
        return redirect(home)

    return render(request, 'deletarH.html', {'cadastrado': cadastrado})


@login_required
def cadastrar_horario(request):
    Mhora = Horariodisponivel(request.POST or None)
    if Mhora.is_valid():
        Mhora.save()
        return redirect(home)

    return render(request, 'cadastrar_horario.html', {'Mhora': Mhora})


@login_required
def alterar(request, id):
    marcar = Professor.objects.get(id=id)
    Mhora = Horariodisponivel(request.POST or None, instance=marcar)
    if Mhora.is_valid():
        Mhora.save()
        return redirect(home)

    return render(request, 'cadastrar_horario.html', {'Mhora': Mhora, 'marcar': marcar})


@login_required
def deletar(request, id):
    cadastrado = Professor.objects.get(id=id)
    if request.method == 'POST':
        cadastrado.delete()
        return redirect(home)

    return render(request, 'deletar.html', {'cadastrado': cadastrado})


def aluno(request):
    hora = Professor.objects.all()
    return render(request, 'aluno.html', {'hora': hora})


def agenda_hora(request):
    agendaH = Alunofazercomentario(request.POST or None)
    if agendaH.is_valid():
        agendaH.save()
        return redirect(home)

    return render(request, 'agenda_hora.html', {'agendaH': agendaH})


def deletar_comentario(request, id):
    cadastrado = Comentario.objects.get(id=id)
    if request.method == 'POST':
        cadastrado.delete()
        return redirect(home)

    return render(request, 'deletarC.html', {'cadastrado': cadastrado})


def alterar_comentario(request, id):
    agenda = Comentario.objects.get(id=id)
    agendaH = Alunofazercomentario(request.POST or None, instance=agenda)
    if agendaH.is_valid():
        agendaH.save()
        return redirect(home)
    return render(request, 'agenda_hora.html', {'agendaH': agendaH, 'agenda': agenda})


def comentarios(request):
    hora = Comentario.objects.all()
    return render(request, 'comentarios.html', {'hora': hora})

def comentarioA(request):
    hora = Comentario.objects.all()
    return render(request, 'comentariosAluno.html', {'hora': hora})


###########################################################################################

def confirmar(request, id):
    marcar = Professor.objects.get(id=id)
    disp = Alunodisponivelizar(request.POST or None,instance=marcar)
    dis = Alunodisponivelizar(request.POST or None)
    if request.method == 'POST':
        disp.save()
        dis.save()
        return redirect(home)

    return render(request, 'novo.html', {'disp': disp})


def com_atendimento(request):
    hora = Aluno.objects.all()
    return render(request, 'confirmacao.html', {'hora': hora})
