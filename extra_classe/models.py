from django.db import models


class Profdisciplina(models.Model):
    nome_professor = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_professor


class Disciplina(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Professor(models.Model):
    nome_professor = models.ForeignKey(Profdisciplina, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    data = models.DateField(max_length=20)
    hora = models.TimeField(max_length=20)

class Atendimento(models.Model):
    nome_professor = models.ForeignKey(Profdisciplina, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    data = models.DateField(max_length=20)
    hora = models.TimeField(max_length=20)


class Comentario(models.Model):
    nome_aluno = models.CharField(max_length=100)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    duvidas = models.CharField(max_length=500)

class Aluno(models.Model):
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    Confirmar = models.BooleanField(default=True)
