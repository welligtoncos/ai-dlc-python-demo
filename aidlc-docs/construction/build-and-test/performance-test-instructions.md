# Performance Test Instructions

## Status

**N/A para PoC v1** — requisitos de performance não foram definidos em `requirements.md`.

## Contexto

A API Task Manager é uma demonstração AI-DLC com SQLite local e sem requisitos de throughput ou latência. Testes de carga não fazem parte dos critérios de aceite v1.

## Teste manual opcional (smoke)

Se desejar uma verificação informal de latência local:

### 1. Subir a API

```bash
uvicorn app.main:app --port 8000
```

### 2. Requisições repetidas (PowerShell)

```powershell
1..50 | ForEach-Object {
  Invoke-RestMethod -Uri http://localhost:8000/tasks -Method Get
}
```

### 3. Observação

Em ambiente local, `GET /tasks` com poucas dezenas de registros deve responder em milissegundos. Resultados não são benchmark oficial.

## Quando adicionar performance tests

Considere ferramentas como **locust** ou **k6** se no futuro houver:

- Requisito de latência p95 (ex.: &lt; 200 ms)
- Meta de requisições/segundo
- Deploy em produção com múltiplos workers

Até lá, esta fase permanece **N/A**.
