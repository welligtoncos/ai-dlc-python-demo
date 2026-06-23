# Requirements Clarification Questions — Task Manager API

Projeto: **API REST de Gerenciador de Tarefas** (FastAPI + SQLite + SQLModel + pytest).

**Status**: Todas as perguntas respondidas em 2026-06-22.

---

## Question 1
Como deve funcionar o **PUT /tasks/{id}**?

A) Substituição completa — o corpo deve incluir todos os campos editáveis (`titulo`, `descricao`, `concluida`); campos omitidos são rejeitados ou tratados como inválidos

B) Atualização parcial — apenas os campos enviados no JSON são alterados; os demais permanecem inalterados

C) Substituição completa com defaults — campos omitidos assumem valores padrão (`descricao` → `null`, `concluida` → `false`)

X) Other (please describe after [Answer]: tag below)

[Answer]: B

---

## Question 2
Validação de **titulo vazio**: como tratar espaços em branco?

A) Rejeitar se, após `strip()`, o título ficar vazio (recomendado)

B) Rejeitar apenas string literal vazia `""` (espaços são aceitos)

X) Other (please describe after [Answer]: tag below)

[Answer]: A

---

## Question 3
Qual formato e fuso para **criada_em**?

A) `datetime` UTC em ISO 8601 na resposta JSON (ex.: `"2026-06-22T14:00:00Z"`)

B) `datetime` local do servidor, sem timezone na serialização

C) Apenas data, sem hora (`YYYY-MM-DD`)

X) Other (please describe after [Answer]: tag below)

[Answer]: A

---

## Question 4
Resposta do **DELETE /tasks/{id}** em caso de sucesso?

A) `204 No Content` — corpo vazio

B) `200 OK` — corpo JSON com mensagem de confirmação

X) Other (please describe after [Answer]: tag below)

[Answer]: A

---

## Question 5
Estrutura de pastas do código Python?

A) Layout simples na raiz — `main.py`, `models.py`, `database.py`, `tests/`

B) Pacote `app/` — `app/main.py`, `app/models.py`, `app/routers/tasks.py`, `tests/`

C) Pacote `src/task_manager/` com `pyproject.toml` (estrutura publicável)

X) Other (please describe after [Answer]: tag below)

[Answer]: B

---

## Question 6
Local do arquivo SQLite?

A) `tasks.db` na raiz do projeto (desenvolvimento)

B) Caminho configurável via variável de ambiente (ex.: `DATABASE_URL` ou `SQLITE_PATH`)

C) `:memory:` nos testes e arquivo em disco apenas em runtime/dev

X) Other (please describe after [Answer]: tag below)

[Answer]: B

---

## Question 7
Comportamento do **GET /tasks** (listagem)?

A) Retornar todas as tarefas sem ordenação garantida

B) Ordenar por `criada_em` decrescente (mais recentes primeiro)

C) Ordenar por `id` crescente

X) Other (please describe after [Answer]: tag below)

[Answer]: B

---

## Question 8 — Security Extensions
Deseja aplicar as regras da extensão **Security Baseline** neste projeto?

A) Yes — enforce all SECURITY rules as blocking constraints (recommended for production-grade applications)

B) No — skip all SECURITY rules (suitable for PoCs, prototypes, and experimental projects)

X) Other (please describe after [Answer]: tag below)

[Answer]: B

---

## Question 9 — Resiliency Extensions
Deseja aplicar a extensão **Resiliency Baseline**?

A) Yes — apply the resiliency baseline as directional best practices and design-time guidance

B) No — skip the resiliency baseline (suitable for PoCs, prototypes, and experimental projects)

X) Other (please describe after [Answer]: tag below)

[Answer]: B

---

## Question 10 — Property-Based Testing Extension
Deseja aplicar regras de **Property-Based Testing (PBT)**?

A) Yes — enforce all PBT rules as blocking constraints

B) Partial — enforce PBT rules only for pure functions and serialization round-trips

C) No — skip all PBT rules (unit tests with pytest only)

X) Other (please describe after [Answer]: tag below)

[Answer]: C

---

## Requisitos já confirmados (não requer resposta)

| Área | Decisão |
|------|---------|
| Stack | FastAPI + SQLite + SQLModel + pytest |
| Recurso | `Task` |
| Campos | `id` (auto), `titulo` (obrigatório), `descricao` (opcional), `concluida` (bool, default `false`), `criada_em` (auto) |
| Endpoints | POST/GET/GET{id}/PUT/DELETE em `/tasks` |
| POST | Retorna `201 Created` |
| GET/PUT/DELETE por id | `404` se não existir |
| Regra de negócio | `titulo` não pode ser vazio |
| Fora de escopo | Autenticação, usuários, paginação |
