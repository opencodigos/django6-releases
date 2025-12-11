# Django 6 - Demo das Novidades

Projeto de exemplo testando as principais novidades do **Django 6.0**.

## Requisitos

- Python 3.12+
- Django 6.0

## Instalação

```bash
python -m venv .venv
source .venv/bin/activate
pip install django
python manage.py migrate
python manage.py runserver
```

## Novidades do Django 6 Demonstradas

### 1. Background Tasks (`@task`)

Tarefas em segundo plano nativas, sem precisar de Celery para casos simples.

```python
from django.tasks import task

@task
def processar_tarefa_async(tarefa_id: int):
    # Executa em background
    print(f"Processando tarefa {tarefa_id}")

# Dispara a task
processar_tarefa_async.enqueue(tarefa.id)
```

**Arquivo:** `app/views.py`

**Configuração:** `settings.py`
```python
TASKS = {
    "default": {
        "BACKEND": "django.tasks.backends.immediate.ImmediateBackend",
    }
}
```

---

### 2. Template Partials (`{% partialdef %}` e `{% partial %}`)

Componentes de template reutilizáveis sem precisar de includes separados.

```html
{# Define o componente #}
{% partialdef tarefa_item %}
<div class="card">
    <strong>{{ tarefa.titulo }}</strong>
</div>
{% endpartialdef %}

{# Usa o componente #}
{% for tarefa in tarefas %}
    {% partial tarefa_item %}
{% endfor %}
```

**Arquivo:** `app/templates/app/home.html`

---

### 3. Content Security Policy (CSP)

Middleware nativo para proteção contra XSS e injeções.

```python
MIDDLEWARE = [
    'django.middleware.csp.ContentSecurityPolicyMiddleware',
    # ...
]

CONTENT_SECURITY_POLICY = {
    "default-src": ["'self'"],
    "style-src": ["'self'", "'unsafe-inline'"],
    "script-src": ["'self'"],
    "img-src": ["'self'", "data:"],
}
```

**Arquivo:** `core/settings.py`

---

### 4. `forloop.length` em Templates

Novo atributo que retorna o total de itens durante iteração.

```html
{% for tarefa in tarefas %}
    Item {{ forloop.counter }} de {{ forloop.length }}
{% endfor %}
```

**Arquivo:** `app/templates/app/home.html`

---

## URLs

| URL | Descrição |
|-----|-----------|
| `/` | Lista de tarefas |
| `/criar/` | Criar nova tarefa |
| `/toggle/<id>/` | Alternar status |
| `/api/tarefas/` | API JSON |
| `/admin/` | Admin Django |

## Estrutura

```
django6/
├── app/
│   ├── models.py      # Model Tarefa
│   ├── views.py       # Views + @task
│   ├── urls.py        # Rotas
│   ├── admin.py       # Admin
│   └── templates/app/
│       ├── base.html
│       ├── home.html  # Partials + forloop.length
│       └── criar.html
├── core/
│   ├── settings.py    # CSP + TASKS config
│   └── urls.py
└── manage.py
```

## Referências

- [Django 6.0 Release Notes](https://docs.djangoproject.com/en/6.0/releases/6.0/)
- [Background Tasks](https://docs.djangoproject.com/en/6.0/topics/background-tasks/)
- [Template Partials](https://docs.djangoproject.com/en/6.0/ref/templates/builtins/#partialdef)
- [CSP Middleware](https://docs.djangoproject.com/en/6.0/ref/middleware/#content-security-policy)
