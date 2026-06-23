# Integration Test Instructions

## Purpose

Validar o fluxo completo **HTTP → FastAPI → SQLModel → SQLite** para o recurso `Task`, sem mocks da camada de persistência.

Nesta PoC, os testes em `tests/test_tasks.py` já funcionam como **testes de integração de API**: usam `TestClient` real contra a aplicação FastAPI com banco SQLite em memória.

## Test Scenarios

### Scenario 1: Ciclo de vida completo de uma tarefa

- **Description**: Criar → listar → buscar → atualizar parcialmente → deletar
- **Setup**: Fixture `client` (banco isolado por teste)
- **Steps**:
  1. `POST /tasks` com `{"titulo": "Integração"}`
  2. `GET /tasks` — verificar presença na lista
  3. `GET /tasks/{id}` — verificar campos
  4. `PUT /tasks/{id}` com `{"concluida": true}`
  5. `DELETE /tasks/{id}`
  6. `GET /tasks/{id}` — esperar 404
- **Expected**: Status 201 → 200 → 200 → 200 → 204 → 404

### Scenario 2: Validação e erros HTTP

- **Description**: Título inválido e recurso inexistente
- **Steps**:
  1. `POST /tasks` com `{"titulo": "   "}` → 422
  2. `GET /tasks/99999` → 404
  3. `DELETE /tasks/99999` → 404
- **Expected**: Códigos de erro conforme `requirements.md` §4

## Setup Integration Test Environment

### 1. Dependências

```bash
pip install -r requirements.txt
```

### 2. Banco de teste

Configurado automaticamente em `tests/conftest.py`:

- Engine: `sqlite://` (memória)
- `poolclass=StaticPool` para sessão compartilhada no teste
- `dependency_overrides` substitui `get_session` da aplicação

Não é necessário subir serviços externos.

## Run Integration Tests

```bash
pytest tests/test_tasks.py -v
```

## Verificação manual (opcional)

Com a API rodando contra arquivo em disco:

```bash
uvicorn app.main:app --reload --port 8000
```

Em outro terminal:

```bash
curl -X POST http://localhost:8000/tasks -H "Content-Type: application/json" -d "{\"titulo\": \"Manual\"}"
curl http://localhost:8000/tasks
```

## Cleanup

- Testes automatizados: banco em memória descartado ao fim de cada teste
- Teste manual: remover `tasks.db` se desejar resetar dados de dev

```bash
# Windows
del tasks.db

# Linux/macOS
rm -f tasks.db
```
