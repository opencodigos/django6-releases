from django.contrib import admin
from .models import Tarefa


@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'concluida', 'criada_em']
    list_filter = ['concluida']
    search_fields = ['titulo']
