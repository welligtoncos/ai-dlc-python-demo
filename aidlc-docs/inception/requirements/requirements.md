# Requirements — Task Manager REST API

## Intent Analysis

| Campo | Valor |
|-------|-------|
| **User Request** | API REST de Gerenciador de Tarefas em Python com FastAPI, SQLite, SQLModel e testes pytest |
| **Request Type** | Novo projeto |
| **Scope Estimate** | Componente único (recurso `Task`) com 5 endpoints CRUD |
| **Complexity Estimate** | Moderada |
| **Requirements Depth** | Standard |

---

## 1. Visão geral

Construir uma API REST para gerenciamento de tarefas (`Task`), permitindo criar, listar, consultar, atualizar e remover tarefas. Projeto de demonstração AI-DLC, sem autenticação nem multi-tenancy.

### 1.1 Objetivos

- Expor CRUD completo via HTTP/JSON
- Persistir dados em SQLite via SQLModel
- Garantir validação de regras de negócio (`titulo` obrigatório)
- Cobrir comportamento com testes unitários (pytest)

### 1.2 Fora de escopo (v1)

- Autenticação e autorização
- Usuários / multi-tenant
- Paginação, filtros e busca
- Property-based testing (extensão desabilitada)

---

## 2. Stack tecnológica

| Camada | Tecnologia |
|--------|------------|
| Framework HTTP | FastAPI |
| ORM / modelos | SQLModel |
| Banco de dados | SQLite |
| Testes | pytest |
| Documentação API | OpenAPI automática (FastAPI `/docs`) |

---

## 3. Modelo de dados — `Task`

| Campo | Tipo | Obrigatório | Default | Observações |
|-------|------|-------------|---------|-------------|
| `id` | `int` | — | auto | Chave primária, gerada pelo banco |
| `titulo` | `str` | Sim | — | Não pode ser vazio após `strip()` |
| `descricao` | `str \| null` | Não | `null` | Opcional |
| `concluida` | `bool` | Não | `false` | Indica se a tarefa foi concluída |
| `criada_em` | `datetime` | — | auto | Definido na criação; UTC |

### 3.1 Regras de validação

- **FR-VAL-01**: `titulo` é obrigatório em criação (`POST`).
- **FR-VAL-02**: `titulo` não pode ficar vazio após remoção de espaços (`strip()`); requisições com título só com espaços devem retornar **422 Unprocessable Entity**.
- **FR-VAL-03**: Em atualização parcial (`PUT`), se `titulo` for enviado, aplica-se a mesma regra de `strip()` e não-vazio.
- **FR-VAL-04**: `descricao` aceita `null` ou string; sem limite de tamanho definido na v1.
- **FR-VAL-05**: `concluida` aceita apenas valores booleanos.

### 3.2 Serialização de `criada_em`

- **FR-DT-01**: Armazenar e retornar em **UTC**.
- **FR-DT-02**: Serializar em JSON como ISO 8601 com sufixo `Z` (ex.: `"2026-06-22T14:00:00Z"`).
- **FR-DT-03**: `criada_em` é definido automaticamente na criação e **não é editável** via API.

---

## 4. API REST — Endpoints

Base path: `/tasks`

### 4.1 `POST /tasks` — Criar tarefa

| Aspecto | Especificação |
|---------|---------------|
| Corpo | `{ "titulo": string, "descricao"?: string \| null, "concluida"?: bool }` |
| Sucesso | **201 Created** — corpo com objeto `Task` completo |
| Erro validação | **422** — título ausente ou vazio após `strip()` |

### 4.2 `GET /tasks` — Listar tarefas

| Aspecto | Especificação |
|---------|---------------|
| Sucesso | **200 OK** — array JSON de `Task` |
| Ordenação | Por `criada_em` **decrescente** (mais recentes primeiro) |
| Paginação | Não aplicável (fora de escopo) |

### 4.3 `GET /tasks/{id}` — Buscar por ID

| Aspecto | Especificação |
|---------|---------------|
| Sucesso | **200 OK** — objeto `Task` |
| Não encontrado | **404 Not Found** |

### 4.4 `PUT /tasks/{id}` — Atualizar tarefa (parcial)

| Aspecto | Especificação |
|---------|---------------|
| Semântica | **Atualização parcial** — apenas campos presentes no JSON são alterados |
| Campos editáveis | `titulo`, `descricao`, `concluida` |
| Campos não editáveis | `id`, `criada_em` |
| Sucesso | **200 OK** — objeto `Task` atualizado |
| Não encontrado | **404 Not Found** |
| Erro validação | **422** — se `titulo` enviado e inválido (vazio após `strip()`) |

**Exemplo**: `PUT /tasks/1` com `{ "concluida": true }` altera apenas `concluida`; `titulo` e `descricao` permanecem inalterados.

### 4.5 `DELETE /tasks/{id}` — Remover tarefa

| Aspecto | Especificação |
|---------|---------------|
| Sucesso | **204 No Content** — corpo vazio |
| Não encontrado | **404 Not Found** |

---

## 5. Requisitos não funcionais

### 5.1 Estrutura do projeto

Layout com pacote `app/`:

```text
app/
├── main.py           # Instância FastAPI, lifespan, inclusão de routers
├── models.py         # Modelo SQLModel Task (tabela + schemas)
├── database.py       # Engine SQLite, session, init DB
└── routers/
    └── tasks.py      # Endpoints CRUD /tasks
tests/
├── conftest.py       # Fixtures (client, DB de teste)
└── test_tasks.py     # Testes unitários/integração dos endpoints
```

### 5.2 Configuração do banco

- **NFR-DB-01**: Caminho do SQLite configurável via variável de ambiente (`DATABASE_URL` ou `SQLITE_PATH`).
- **NFR-DB-02**: Valor padrão em desenvolvimento: `sqlite:///./tasks.db` (ou equivalente).
- **NFR-DB-03**: Testes devem usar banco isolado (ex.: SQLite em memória ou arquivo temporário) para não poluir dados de dev.

### 5.3 Testabilidade

- **NFR-TEST-01**: Testes com **pytest** cobrindo todos os endpoints CRUD.
- **NFR-TEST-02**: Cenários mínimos: criar (201), listar ordenado, buscar existente/inexistente (200/404), atualizar parcial (200/404/422), deletar (204/404), validação de título vazio.
- **NFR-TEST-03**: Property-Based Testing **desabilitado** (decisão Q10-C).

### 5.4 Manutenibilidade

- **NFR-MAINT-01**: Separação clara entre modelos, persistência, rotas e testes.
- **NFR-MAINT-02**: Dependências declaradas em `requirements.txt` ou `pyproject.toml`.

### 5.5 Extensões AI-DLC

| Extensão | Habilitada | Decisão |
|----------|------------|---------|
| Security Baseline | Não | Q8-B — PoC/demo |
| Resiliency Baseline | Não | Q9-B — PoC/demo |
| Property-Based Testing | Não | Q10-C — apenas pytest unitário |

---

## 6. Cenários e casos de borda

| ID | Cenário | Resultado esperado |
|----|---------|-------------------|
| SC-01 | POST com `titulo` válido | 201 + Task com `id`, `criada_em`, `concluida=false` |
| SC-02 | POST sem `titulo` | 422 |
| SC-03 | POST com `titulo: "   "` | 422 |
| SC-04 | GET /tasks com N tarefas | 200, ordenadas por `criada_em` desc |
| SC-05 | GET /tasks/999 inexistente | 404 |
| SC-06 | PUT parcial só `concluida` | 200, demais campos preservados |
| SC-07 | PUT com `titulo: ""` | 422 |
| SC-08 | DELETE tarefa existente | 204 |
| SC-09 | DELETE tarefa inexistente | 404 |

---

## 7. Critérios de aceite (v1)

- [ ] Todos os 5 endpoints implementados conforme seção 4
- [ ] Modelo `Task` persistido em SQLite via SQLModel
- [ ] Validação de `titulo` com `strip()` em POST e PUT
- [ ] `criada_em` em UTC, ISO 8601 com `Z`
- [ ] `GET /tasks` ordenado por `criada_em` decrescente
- [ ] `DELETE` retorna 204 sem corpo
- [ ] Suite pytest passando para cenários da seção 6
- [ ] README atualizado com instruções de execução

---

## 8. Rastreabilidade das respostas

| Pergunta | Resposta | Requisito derivado |
|----------|----------|-------------------|
| Q1 | B | PUT parcial (§4.4) |
| Q2 | A | Validação `strip()` (§3.1) |
| Q3 | A | UTC ISO 8601 (§3.2) |
| Q4 | A | DELETE 204 (§4.5) |
| Q5 | B | Layout `app/` (§5.1) |
| Q6 | B | DB via env var (§5.2) |
| Q7 | B | Ordenação `criada_em` desc (§4.2) |
| Q8 | B | Security Baseline off (§5.5) |
| Q9 | B | Resiliency Baseline off (§5.5) |
| Q10 | C | Apenas pytest (§5.3) |

---

## 9. Referências

- Perguntas respondidas: `aidlc-docs/inception/requirements/requirement-verification-questions.md`
- Estado do projeto: `aidlc-docs/aidlc-state.md`
