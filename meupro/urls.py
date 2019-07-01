"""meupro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from extra_classe.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),

    path('', home,name='home'),
    path('home', home,name='home'),
    path('professor/', professor,name='professor'),
    path('cadastrar_horario/', cadastrar_horario,name='cadastrar_horario'),
    path('deletar_horario/<int:id>/', deletar, name='deletar_horario'),
    path('alterar_horario/<int:id>/', alterar, name='alterar_horario'),
    path('salvar/<int:id>/', salvar, name='salvar'),
    path('aluno/', aluno,name='aluno'),
    path('agenda_hora/', agenda_hora,name='agenda_hora'),
    path('com_atendimento/', com_atendimento,name='com_atendimento'),
    path('comentario_alunos/', comentarioA,name='comentario_alunos'),

    path('confirmar/<int:id>/', confirmar,name='confirmar'),


    path('comentarios/', comentarios,name='comentarios'),
    path('mostrar/', mostrar,name='mostrar'),
    path('delete_h_marcado/<int:id>/', apaga, name='delete_h_marcado'),
    path('deletar_comentario/<int:id>/', deletar_comentario, name='deletar_comentario'),
    path('alterar_comentario/<int:id>/', alterar_comentario, name='alterar_comentario'),
]
