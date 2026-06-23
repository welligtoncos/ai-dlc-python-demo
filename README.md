# ai-dlc-python-demo

Demonstração do workflow **AI-DLC** (AI-Driven Development Life Cycle) com Python: API REST de gerenciamento de tarefas construída com planejamento guiado por IA.

Repositório: [github.com/welligtoncos/ai-dlc-python-demo](https://github.com/welligtoncos/ai-dlc-python-demo)

## Task Manager API

API REST CRUD para o recurso `Task`, implementada com **FastAPI**, **SQLModel** e **SQLite**.

### Endpoints

| Método | Rota | Descrição |
|--------|------|-----------|
| `POST` | `/tasks` | Criar tarefa (201) |
| `GET` | `/tasks` | Listar todas (ordenadas por `criada_em` desc) |
| `GET` | `/tasks/{id}` | Buscar por ID (404 se não existir) |
| `PUT` | `/tasks/{id}` | Atualizar parcialmente (404 se não existir) |
| `DELETE` | `/tasks/{id}` | Remover (204, 404 se não existir) |

Documentação interativa: `http://localhost:8000/docs`

### Modelo `Task`

| Campo | Tipo | Observações |
|-------|------|-------------|
| `id` | int | Auto-gerado |
| `titulo` | string | Obrigatório; não vazio após `strip()` |
| `descricao` | string \| null | Opcional |
| `concluida` | bool | Padrão `false` |
| `criada_em` | datetime | UTC, ISO 8601 com `Z` |

## Estrutura do projeto

```text
.
├── app/
│   ├── main.py
│   ├── models.py
│   ├── database.py
│   └── routers/
│       └── tasks.py
├── tests/
│   ├── conftest.py
│   └── test_tasks.py
├── requirements.txt
└── aidlc-docs/          # Documentação AI-DLC
```

## Desenvolvimento

```bash
# Ambiente virtual
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # Linux/macOS

# Dependências
pip install -r requirements.txt

# Executar API
uvicorn app.main:app --reload

# Testes
pytest
```

### Variáveis de ambiente

| Variável | Padrão | Descrição |
|----------|--------|-----------|
| `DATABASE_URL` | `sqlite:///./tasks.db` | Conexão SQLite |

## AI-DLC

Documentação do workflow em `aidlc-docs/`:

- Requisitos: `aidlc-docs/inception/requirements/requirements.md`
- Plano de execução: `aidlc-docs/inception/plans/execution-plan.md`
- Estado: `aidlc-docs/aidlc-state.md`

## Autor

[Welligton](https://github.com/welligtoncos)
