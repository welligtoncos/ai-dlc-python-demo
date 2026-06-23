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

## Por que usar o AI-DLC?

Depois de rodar o fluxo inteiro (como nesta PoC), a avaliação fica baseada na prática — não na propaganda. Os motivos principais, em ordem de peso:

### 1. Controle real sobre a IA (o motivo nº 1)

Sem AI-DLC, você pede algo e a IA decide sozinha — inclusive escolhas que você nem sabia que estavam sendo tomadas. Nesta PoC, o processo **forçou** decisões explícitas: `strip()` no título, formato UTC da data, `204` no DELETE, PUT parcial. Num fluxo comum, a IA chutaria e você só descobriria o problema depois.

O AI-DLC inverte isso: **a IA propõe, você aprova, em cada gate**. Você não fica refém de 30 minutos de código na direção errada.

### 2. Menos retrabalho

Corrigir uma decisão no `requirements.md` custa segundos. Corrigir a mesma decisão depois que virou código, testes e dependências custa horas. O AI-DLC empurra decisões para **antes** do processo, onde errar é barato — o custo de um erro cresce exponencialmente conforme avança no ciclo.

### 3. Documentação que nasce sozinha

A pasta `aidlc-docs/` deste repositório é documentação real, rastreável e versionável — sem você escrever do zero. Serve para onboarding, para justificar *"por que fizemos assim"* meses depois, ou para auditoria. O `audit.md` registra o raciocínio das decisões, algo que normalmente se perde em chats ou na cabeça de quem saiu.

### 4. Padronização e imposição de regras

Com o mesmo conjunto de regras, o processo fica consistente entre devs. Extensões **bloqueantes** (veja seção de customização) transformam boas práticas esquecidas em **gates que travam o fluxo** — segurança, compliance e convenções da empresa viram regras que a IA não ignora.

### 5. Independência de fornecedor

O AI-DLC é agnóstico: Cursor, Claude Code, Amazon Q, Copilot. Trocou de IDE? As regras vão junto (`.cursor/rules/` + `.aidlc-rule-details/`). Sendo open source (MIT-0), você customiza sem amarras legais.

### Em uma frase

> O AI-DLC transforma a IA de um *"gerador que adivinha o que você quer"* em um *"engenheiro disciplinado que confirma antes de agir e documenta o porquê"*.

**O que você troca:** um pouco de velocidade bruta em favor de **controle**, **rastreabilidade** e **menos retrabalho**.

### Quando NÃO usar (seja honesto)

| Situação | Recomendação |
|----------|--------------|
| Fix de uma linha, ajuste trivial, script descartável | **Não use** — overhead puro |
| Feature nova de complexidade média/alta | **Use** |
| Projeto do zero, código desconhecido, requisitos nebulosos | **Use** — errar a direção sai caro |

Para tarefa pequena: peça código direto. Para tarefa que importa: use o processo.

**Equilíbrio adaptativo:** nesta PoC, o plano **pulou 8 de 10 etapas** porque o escopo era simples. Você não paga o processo completo à toa — o sistema se auto-enxuga.

### Regra de decisão

```text
Use AI-DLC quando o custo de errar a direção > custo do processo.
```

Para um dev experiente, o maior valor muitas vezes **não é o código** — é a disciplina imposta à IA e a documentação que sobra de graça.

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

### Extensões opcionais (já incluídas)

Durante Requirements Analysis, a IA pergunta sobre extensões em `.aidlc-rule-details/extensions/`:

- **Security Baseline** — `extensions/security/baseline/`
- **Resiliency Baseline** — `extensions/resiliency/baseline/`
- **Property-Based Testing** — `extensions/testing/property-based/`

Para PoCs, costuma-se responder **No**. Para criar **suas próprias** regras, veja a seção abaixo.

---

## Como customizar o AI-DLC (criar e editar regras)

Como tudo no AI-DLC é **texto (markdown)**, você molda o comportamento do agente editando arquivos de regras — sem recompilar nada. Esse é o ponto em que a metodologia brilha: você adapta o processo ao seu time, stack ou compliance.

### A regra de ouro: extensões, não o núcleo

Há duas formas de mexer. A **ordem de preferência** importa:

| Abordagem | Onde | Quando usar | Risco |
|-----------|------|-------------|-------|
| **Extensão** (recomendado) | `.aidlc-rule-details/extensions/` | Regras do seu time, qualidade, compliance | Baixo — isolado, sobrevive a updates |
| **Núcleo** (avançado) | `.cursor/rules/ai-dlc-workflow.mdc` | Mudar o fluxo principal da metodologia | Alto — quebra fácil; conflita com updates |

**Por que preferir extensões?**

- Você **não toca** no núcleo da metodologia
- Suas regras ficam **por cima** do workflow padrão
- Quando sair atualização do AI-DLC, o núcleo atualiza sem você refazer mudanças na mão
- Ganha de graça o sistema de **opt-in** (pergunta na Requirements Analysis)
- Regras ativas são **bloqueantes** — o estágio não avança até a verificação passar

Editar `ai-dlc-workflow.mdc` funciona, mas um erro ali pode quebrar o comportamento inteiro. Use só se souber exatamente o que está mudando no fluxo.

### Caminho seguro: criar sua própria extensão

Uma extensão são **dois arquivos** na mesma pasta dentro de `.aidlc-rule-details/extensions/`.

Exemplo: regra de qualidade de código em `qualidade/codigo-limpo/`.

#### Passo 1 — Criar a pasta

```text
.aidlc-rule-details/extensions/
└── qualidade/
    └── codigo-limpo/
        ├── codigo-limpo.md          # Regras (obrigatório)
        └── codigo-limpo.opt-in.md   # Opt-in (opcional — ver abaixo)
```

#### Passo 2 — Arquivo de regras (`codigo-limpo.md`)

Cada regra segue o formato:

- Cabeçalho: `## Rule <PREFIXO-NN>: <Título>`
- Seção **Rule:** o que exigir
- Seção **Verification:** como o modelo verifica (checagem concreta)

```markdown
# Code Quality Rules

## Rule CQ-01: Funções pequenas e focadas
**Rule:** Cada função deve ter responsabilidade única e no máximo ~30 linhas.
**Verification:** Verifique se nenhuma função excede 30 linhas ou mistura
responsabilidades distintas. Se exceder, sinalize antes de prosseguir.

## Rule CQ-02: Sem números mágicos
**Rule:** Valores literais devem ser constantes nomeadas.
**Verification:** Verifique se há literais numéricos não óbvios no código;
se houver, exija que sejam extraídos para constantes.
```

Os IDs (`CQ-01`, `CQ-02`) devem ser **únicos** entre todas as extensões — aparecem nos logs de `aidlc-docs/audit.md`.

**Dica:** copie a estrutura de [security-baseline.md](.aidlc-rule-details/extensions/security/baseline/security-baseline.md) (modelo de referência AWS) e adapte ao seu caso. É o atalho mais rápido para acertar o formato.

#### Passo 3 — Arquivo de opt-in (`codigo-limpo.opt-in.md`)

Contém a pergunta de múltipla escolha exibida na **Requirements Analysis**. Use [security-baseline.opt-in.md](.aidlc-rule-details/extensions/security/baseline/security-baseline.opt-in.md) como molde.

Estrutura do arquivo:

- Título `# Nome — Opt-In`
- Campo `**Extension**:` com nome legível
- Seção `## Opt-In Prompt` com a pergunta em markdown (opções A, B, X e `[Answer]:`)

Exemplo da pergunta dentro do opt-in:

```text
## Question: Code Quality Extensions
Should code quality rules be enforced for this project?

A) Yes — enforce all CQ rules as blocking constraints
B) No — skip all CQ rules
X) Other (please describe after [Answer]: tag below)

[Answer]:
```

#### Passo 4 — Recarregar

1. Abra um **chat novo** no Cursor (sessão limpa)
2. Rode `Using AI-DLC, ...` na sua tarefa
3. Na Requirements Analysis, sua extensão deve aparecer nas perguntas de opt-in

A escolha fica registrada em `aidlc-docs/aidlc-state.md` → `## Extension Configuration`.

### Opt-in vs. sempre-ativo

| Configuração | Arquivos | Comportamento |
|--------------|----------|---------------|
| **Opcional** | `.md` + `.opt-in.md` | IA pergunta se você quer ativar na Requirements Analysis |
| **Sempre ativo** | só `.md` (sem `.opt-in.md`) | Regra aplicada em todo workflow, sem opção de desligar |

Em **ambos** os casos, uma vez ativa, a regra é **bloqueante**: o estágio não conclui até a verificação passar. Ideal para padrões inegociáveis (segurança da empresa, compliance, qualidade mínima).

### Caminho avançado: editar o núcleo

Arquivo: `.cursor/rules/ai-dlc-workflow.mdc`

Use apenas para:

- Ajustar quais fases são obrigatórias vs. condicionais
- Mudar mensagens de boas-vindas ou gates de aprovação
- Integrar comportamento que não cabe em uma extensão pontual

**Cuidados:**

- Faça backup ou use git antes de editar
- Após update do pacote AI-DLC, compare e re-aplique mudanças manualmente
- Prefira extensões para regras de código, segurança e qualidade

Regras detalhadas por fase ficam em `.aidlc-rule-details/` (ex.: `inception/requirements-analysis.md`, `construction/code-generation.md`). Edite esses arquivos só se quiser mudar **como cada estágio executa**, não apenas **o que o código deve obedecer**.

### Como testar que sua regra funciona

1. Crie a extensão e abra um **chat novo**
2. Rode uma tarefa pequena: `Using AI-DLC, ...`
3. Na Requirements Analysis, confirme que sua pergunta de opt-in apareceu
4. Ative a extensão (resposta **A**)
5. Force uma violação de propósito (ex.: peça uma função gigante se CQ-01 limita a 30 linhas)
6. Verifique se o AI-DLC **bloqueia** o estágio citando seu ID (`CQ-01`) e pede correção

| Resultado | O que fazer |
|-----------|-------------|
| Bloqueou e citou o ID | Regra funcionando |
| Passou batido | Seção **Verification** provavelmente vaga — torne o critério binário e checável |

### Como escrever boas regras

A seção **Verification** é onde tudo acontece.

| Ruim (vago) | Bom (checável) |
|-------------|----------------|
| "Garanta qualidade" | "Verifique se nenhuma função excede 30 linhas" |
| "Código seguro" | "Verifique se não há SQL concatenado com input do usuário" |
| "Boa cobertura de testes" | "Verifique se cada endpoint público tem pelo menos um teste de sucesso e um de erro" |

Pense na Verification como um **teste automatizado em linguagem natural**: quanto mais concreto e binário o critério, mais confiável o bloqueio.

### Referência rápida — extensões existentes

| Extensão | Pasta | Prefixo de regras |
|----------|-------|-------------------|
| Security Baseline | `extensions/security/baseline/` | `SECURITY-NN` |
| Resiliency Baseline | `extensions/resiliency/baseline/` | (ver arquivo `.md`) |
| Property-Based Testing | `extensions/testing/property-based/` | (ver arquivo `.md`) |

Abra os pares `*.md` + `*.opt-in.md` dessas pastas antes de criar a sua — é o template oficial do formato.

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
├── .cursor/rules/            # Núcleo AI-DLC (editar com cuidado)
├── .aidlc-rule-details/      # Regras detalhadas + extensions/
│   ├── inception/              # Regras por fase
│   ├── construction/
│   └── extensions/             # Suas extensões customizadas aqui
└── aidlc-docs/               # Documentação gerada pelo AI-DLC
```

---

## Documentação de referência desta PoC

Esta PoC é o **exemplo concreto** dos motivos acima: requisitos explícitos, plano enxuto, código aprovado, 11 testes passando, `aidlc-docs/` completo.

| Documento | Conteúdo |
|-----------|----------|
| [requirements.md](aidlc-docs/inception/requirements/requirements.md) | Requisitos formais |
| [execution-plan.md](aidlc-docs/inception/plans/execution-plan.md) | Plano de execução |
| [build-and-test-summary.md](aidlc-docs/construction/build-and-test/build-and-test-summary.md) | Resultado de build e testes |
| [aidlc-state.md](aidlc-docs/aidlc-state.md) | Estado final do workflow |
| [audit.md](aidlc-docs/audit.md) | Trilha de decisões e aprovações |

---

## Autor

[Welligton](https://github.com/welligtoncos)
