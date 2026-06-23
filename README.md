# ai-dlc-python-demo

Demonstração do **AI-DLC** (AI-Driven Development Life Cycle) com Python: do planejamento guiado por IA até código e testes com trilha de auditoria completa.

Repositório: [github.com/welligtoncos/ai-dlc-python-demo](https://github.com/welligtoncos/ai-dlc-python-demo)

---

## O que é o AI-DLC?

O AI-DLC é um workflow adaptativo para desenvolvimento de software com IA. Em vez de ir direto ao código, o processo:

- Analisa o workspace (greenfield ou brownfield)
- Levanta e valida requisitos
- Planeja quais etapas executar ou pular
- Gera código e testes com checkpoints de aprovação
- Documenta cada decisão em `aidlc-docs/`

**Princípio:** o workflow se adapta à complexidade — PoCs simples pulam etapas; projetos maiores passam por design, NFR e decomposição em unidades.

---

## Como usar o AI-DLC (passo a passo)

### Pré-requisitos

1. **Cursor** (ou IDE compatível) com a regra do workflow ativa em `.cursor/rules/ai-dlc-workflow.mdc`
2. Regras detalhadas em `.aidlc-rule-details/` (já incluídas neste repositório)
3. Descreva sua solicitação de forma clara: stack, escopo e o que fica **fora** do escopo

### Fase 1 — INCEPTION (planejamento)

| # | Etapa | O que acontece | Sua ação |
|---|--------|----------------|----------|
| 1 | **Workspace Detection** | A IA analisa o projeto (código existente, linguagem, estrutura) | Automático — apenas leia o resumo |
| 2 | **Reverse Engineering** | Só em projetos brownfield (código já existente) | Aprovar artefatos, se executado |
| 3 | **Requirements Analysis** | Perguntas em `aidlc-docs/inception/requirements/requirement-verification-questions.md` | Responda cada `[Answer]:` (A, B, C… ou X) |
| 4 | **User Stories** | Opcional — personas e histórias | Aprovar ou pedir para incluir a etapa |
| 5 | **Workflow Planning** | Plano em `aidlc-docs/inception/plans/execution-plan.md` | Revise skips/executes e **aprove** |
| 6 | **Application Design** | Condicional — componentes e regras | Só se o plano incluir |
| 7 | **Units Generation** | Condicional — decomposição em unidades | Só se o plano incluir |

**Gates de aprovação (obrigatórios):**

- Após requisitos → `✅ Approve & Continue` no `requirements.md`
- Após plano → `✅ Approve & Continue` no `execution-plan.md`

### Fase 2 — CONSTRUCTION (implementação)

| # | Etapa | O que acontece | Sua ação |
|---|--------|----------------|----------|
| 8 | **Functional / NFR / Infrastructure Design** | Condicional por unidade | Aprovar se executado |
| 9 | **Code Generation** | Código em `app/`, testes em `tests/` | Revise o código e **aprove** |
| 10 | **Build and Test** | Instruções em `aidlc-docs/construction/build-and-test/` | Rode `pytest`, revise o summary e **aprove** |

### Fase 3 — OPERATIONS

Placeholder no AI-DLC atual (deploy, monitoramento). Para PoCs, o ciclo encerra após Build and Test.

### Exemplo de prompt inicial

```text
Using AI-DLC, quero construir uma API REST de Gerenciador de Tarefas em Python com FastAPI.

Stack: FastAPI + SQLite + SQLModel + pytest.
Recurso Task com campos: id, titulo, descricao, concluida, criada_em.
Endpoints CRUD em /tasks.
Fora do escopo: autenticação, paginação.

Comece pela fase de Inception levantando os requisitos.
```

### Respostas de aprovação no chat

Use frases explícitas para a IA avançar:

| Momento | Exemplo |
|---------|---------|
| Requisitos OK | `✅ Approve & Continue — pode prosseguir para Workflow Planning` |
| Plano OK | `✅ Approve & Continue — pode prosseguir para Code Generation` |
| Código OK | `✅ Continue to Next Stage — pode prosseguir para Build & Test` |
| Build/Test OK | `✅ Approve & Continue — PoC encerrada` |
| Alteração | `🔧 Request Changes — [descreva o que mudar]` |

### Onde ficam os artefatos

```text
aidlc-docs/
├── aidlc-state.md          # Progresso atual do workflow
├── audit.md                  # Log de todas as interações
├── inception/
│   ├── requirements/         # Perguntas + requirements.md
│   └── plans/                # execution-plan.md
└── construction/
    ├── plans/                # Plano de geração de código
    └── build-and-test/       # Instruções e summary de testes
```

**Regra de ouro:** código da aplicação na **raiz** (`app/`, `tests/`). Documentação do processo apenas em `aidlc-docs/`.

### Extensões opcionais

Durante Requirements Analysis, a IA pergunta sobre:

- **Security Baseline** — regras de segurança bloqueantes
- **Resiliency Baseline** — boas práticas de resiliência
- **Property-Based Testing** — testes baseados em propriedades

Para PoCs, costuma-se responder **No** às três.

---

## Task Manager API (resultado desta PoC)

API REST CRUD para o recurso `Task`, implementada com **FastAPI**, **SQLModel** e **SQLite**.

### Endpoints

| Método | Rota | Descrição |
|--------|------|-----------|
| `POST` | `/tasks` | Criar tarefa (201) |
| `GET` | `/tasks` | Listar todas (ordenadas por `criada_em` desc) |
| `GET` | `/tasks/{id}` | Buscar por ID (404 se não existir) |
| `PUT` | `/tasks/{id}` | Atualizar parcialmente (404 se não existir) |
| `DELETE` | `/tasks/{id}` | Remover (204, 404 se não existir) |

Documentação interativa: http://localhost:8000/docs

### Modelo `Task`

| Campo | Tipo | Observações |
|-------|------|-------------|
| `id` | int | Auto-gerado |
| `titulo` | string | Obrigatório; não vazio após `strip()` |
| `descricao` | string \| null | Opcional |
| `concluida` | bool | Padrão `false` |
| `criada_em` | datetime | UTC, ISO 8601 com `Z` |

---

## Como executar o projeto

### 1. Clonar e entrar na pasta

```bash
git clone https://github.com/welligtoncos/ai-dlc-python-demo.git
cd ai-dlc-python-demo
```

### 2. Ambiente virtual (recomendado)

```bash
python -m venv .venv
```

**Windows:**

```bash
.venv\Scripts\activate
```

**Linux/macOS:**

```bash
source .venv/bin/activate
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Rodar a API

```bash
uvicorn app.main:app --reload
```

Acesse:

- API: http://localhost:8000
- Swagger: http://localhost:8000/docs

### 5. Rodar os testes

```bash
pytest -v
```

Resultado esperado: **11 testes passando**.

### Variáveis de ambiente

| Variável | Padrão | Descrição |
|----------|--------|-----------|
| `DATABASE_URL` | `sqlite:///./tasks.db` | Conexão SQLite (arquivo criado no primeiro run) |

### Exemplo rápido (curl)

```bash
curl -X POST http://localhost:8000/tasks \
  -H "Content-Type: application/json" \
  -d "{\"titulo\": \"Minha tarefa\"}"

curl http://localhost:8000/tasks
```

---

## Estrutura do repositório

```text
.
├── app/                      # Código da API
│   ├── main.py
│   ├── models.py
│   ├── database.py
│   └── routers/tasks.py
├── tests/                    # Testes pytest
├── requirements.txt
├── .cursor/rules/            # Regra AI-DLC para o Cursor
├── .aidlc-rule-details/      # Regras detalhadas do workflow
└── aidlc-docs/               # Documentação gerada pelo AI-DLC
```

---

## Documentação de referência desta PoC

| Documento | Conteúdo |
|-----------|----------|
| [requirements.md](aidlc-docs/inception/requirements/requirements.md) | Requisitos formais |
| [execution-plan.md](aidlc-docs/inception/plans/execution-plan.md) | Plano de execução |
| [build-and-test-summary.md](aidlc-docs/construction/build-and-test/build-and-test-summary.md) | Resultado de build e testes |
| [aidlc-state.md](aidlc-docs/aidlc-state.md) | Estado final do workflow |

---

## Autor

[Welligton](https://github.com/welligtoncos)
