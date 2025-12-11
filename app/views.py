from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.tasks import task  # Django 6 - Background Tasks

from .models import Tarefa


# =============================================================================
# Django 6: Background Tasks com @task
# =============================================================================
@task
def processar_tarefa_async(tarefa_id: int):
    """
    Tarefa em segundo plano (Django 6).
    Simula processamento pesado sem bloquear a requisição.
    """
    import time
    time.sleep(2)  # Simula trabalho pesado
    print(f"✅ Tarefa {tarefa_id} processada em background!")
    return f"Tarefa {tarefa_id} concluída"


def home(request):
    """View principal - lista tarefas usando Template Partials e forloop.length"""
    tarefas = Tarefa.objects.all()
    return render(request, 'app/home.html', {'tarefas': tarefas})


def criar_tarefa(request):
    """Cria tarefa e dispara processamento em background"""
    if request.method == 'POST':
        titulo = request.POST.get('titulo', 'Nova Tarefa')
        tarefa = Tarefa.objects.create(titulo=titulo)
        
        # Django 6: Dispara task em background
        processar_tarefa_async.enqueue(tarefa.id)
        
        return redirect('home')
    return render(request, 'app/criar.html')


def toggle_tarefa(request, pk):
    """Alterna status da tarefa"""
    tarefa = Tarefa.objects.get(pk=pk)
    tarefa.concluida = not tarefa.concluida
    tarefa.save()
    return redirect('home')


def api_tarefas(request):
    """API simples retornando JSON"""
    tarefas = list(Tarefa.objects.values('id', 'titulo', 'concluida'))
    return JsonResponse({'tarefas': tarefas, 'total': len(tarefas)})
