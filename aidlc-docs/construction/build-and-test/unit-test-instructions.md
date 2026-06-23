# Unit Test Execution

## Escopo

Testes unitários e de API em `tests/test_tasks.py`, usando `TestClient` do FastAPI com banco SQLite em memória (fixture em `tests/conftest.py`).

## Run Unit Tests

### 1. Instalar dependências

```bash
pip install -r requirements.txt
```

### 2. Executar todos os testes

```bash
pytest -v
```

Saída verbosa com detalhes por teste:

```bash
pytest -v --tb=short
```

### 3. Executar cenário específico

```bash
pytest tests/test_tasks.py::test_sc01_create_task_returns_201 -v
```

## Resultados esperados

| Métrica | Valor |
|---------|-------|
| **Total de testes** | 11 |
| **Falhas** | 0 |
| **Cenários cobertos** | SC-01 a SC-09 + validação de strip + GET 200 |

## Mapeamento cenário → teste

| Cenário | Teste |
|---------|-------|
| SC-01 | `test_sc01_create_task_returns_201` |
| SC-02 | `test_sc02_create_without_titulo_returns_422` |
| SC-03 | `test_sc03_create_with_blank_titulo_returns_422` |
| SC-04 | `test_sc04_list_tasks_ordered_by_criada_em_desc` |
| SC-05 | `test_sc05_get_nonexistent_task_returns_404` |
| SC-06 | `test_sc06_partial_update_preserves_other_fields` |
| SC-07 | `test_sc07_put_with_empty_titulo_returns_422` |
| SC-08 | `test_sc08_delete_existing_task_returns_204` |
| SC-09 | `test_sc09_delete_nonexistent_task_returns_404` |

## Corrigir testes falhando

1. Ler a saída do pytest (`FAILED` + traceback)
2. Identificar endpoint ou validação afetada
3. Corrigir código em `app/` ou ajustar expectativa do teste
4. Reexecutar `pytest -v` até 11/11 passar

## Cobertura (opcional)

```bash
pip install pytest-cov
pytest --cov=app --cov-report=term-missing
```

Não é obrigatório para a PoC v1.
