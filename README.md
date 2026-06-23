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

## Custo de tokens

Por que consome mais do que um prompt direto — e onde você ganha em relação a isso.

O AI-DLC **gasta mais tokens** que um pedido direto — isso é estrutural, não bug. Entender o porquê ajuda a decidir quando vale a pena.

### Por que consome mais

Em vez de uma única troca (`"escreve a API"` → código), o AI-DLC quebra o trabalho em **várias etapas**, cada uma com pelo menos uma chamada ao modelo.

Nesta PoC, isso incluiu:

| Fase | Atividade (tokens entrada + saída) |
|------|-------------------------------------|
| Inception | Workspace detection, perguntas, `requirements.md`, `execution-plan.md` |
| Construction | Plano de código, geração de `app/` + `tests/`, instruções build/test |
| Contínuo | `audit.md`, `aidlc-state.md`, resumos de aprovação |

**Dois multiplicadores importantes:**

1. **Muito texto gerado** — `requirements.md`, `execution-plan.md`, `audit.md` e resumos são tokens de **saída** que num pedido direto não existiriam.

2. **Contexto relido** — a cada etapa o modelo carrega regras do AI-DLC (ex.: `.cursor/rules/ai-dlc-workflow.mdc`, dezenas de KB) **mais** artefatos das fases anteriores. Esse contexto acumulado entra como tokens de **entrada** repetidamente.

### A magnitude (com honestidade)

Comparado a *"me escreve essa API CRUD"* num único prompt, o AI-DLC consome **várias vezes mais tokens** para produzir o mesmo código final.

Não há número fixo — varia por modelo, tamanho das regras e quantas fases rodam — mas a ordem de grandeza é **"múltiplos"**, não *"uns 10% a mais"*. Você paga por um **processo**, não só por um resultado.

### O que segura o custo

**Inteligência adaptativa:** nesta PoC, o plano **pulou 8 de 10 etapas** por baixa complexidade. O AI-DLC não roda o processo completo cegamente — **se enxuga** conforme a tarefa. Tarefa simples gasta uma fração do que uma complexa gastaria.

Isso evita que o custo vire desperdício automático (desde que você não force etapas desnecessárias).

### Onde você ganha em relação ao custo

A pergunta certa não é *"gasta mais token?"* (gasta), mas **"o que recebo por esses tokens a mais?"**

| Você paga (tokens) | Você recebe |
|--------------------|-------------|
| Múltiplas fases | Decisões certas **cedo** (menos retrabalho caro depois) |
| Documentos gerados | `aidlc-docs/` rastreável **de graça** (onboarding, auditoria, handoff) |
| Gates de aprovação | **Controle** em cada etapa — a IA não chuta `strip()`, UTC, 204 sozinha |
| Revisão humana real | Menos horas corrigindo código na direção errada |

Em tarefa que **importa**, tokens extras podem **economizar dinheiro no fim**: uma decisão errada descoberta tarde (código + testes + dependências) custa muito mais que alguns milhares de tokens na Inception.

Em tarefa **trivial**, é desperdício puro — use pedido direto.

### Regra prática de custo

```text
Vale o token extra quando: custo de errar a direção > custo do processo
Não vale quando: tarefa pequena, direta, e você não vai revisar os gates
```

É a **mesma regra** de quando usar o AI-DLC — custo e benefício andam juntos.

### Lembrete sobre fatura

O **AI-DLC é gratuito** (regras open source). O **agente/modelo por baixo** (Cursor, Claude, Copilot, etc.) **não é** — é ali que tokens viram fatura.

Revise o plano e preços do modelo que você usa. O consumo depende do provedor, não do método em si.

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

## AI-DLC com outro desenvolvedor (handoff e brownfield)

A prova de fogo de qualquer metodologia: **funciona quando outra pessoa pega o projeto?** O AI-DLC tem vantagem real aqui — com armadilhas que vale conhecer.

### O que acontece quando outro dev usa `Using AI-DLC, ...`

No **primeiro ciclo** desta PoC, o agente detectou **greenfield** — sem código, reverse engineering dispensável. Para quem clonar o repo **agora** e pedir uma melhoria, o comportamento é **brownfield**:

| Etapa | Greenfield (você) | Brownfield (outro dev) |
|-------|-------------------|------------------------|
| Workspace Detection | Projeto vazio | Código em `app/`, testes existentes |
| Reverse Engineering | Pulado | **Executado** — mapeia o sistema antes de propor mudanças |
| Requirements / Plano | Do zero | Com **análise de impacto** no que já funciona |
| Gates de aprovação | Iguais | Iguais |

O agente lê `app/`, testes e endpoints atuais **antes** de sugerir alterações — para não quebrar o que já passa em `pytest`.

### O ouro: artefatos que você deixou

A pasta `aidlc-docs/` dá contexto histórico ao próximo dev **e** ao agente:

| Artefato | O que preserva |
|----------|----------------|
| `requirements.md` | O que o sistema deve fazer e **por quê** (PUT parcial, UTC, 204…) |
| `execution-plan.md` | Quais etapas rodaram ou foram puladas |
| `audit.md` | Raciocínio e aprovações de cada gate |
| `aidlc-state.md` | Estado atual do workflow |

O novo dev não precisa adivinhar nem interromper o autor original: *"por que PUT é parcial?"* — está documentado.

### Mesmas regras para todo o time

Com `.cursor/rules/` e `.aidlc-rule-details/extensions/` **versionados no Git**, o outro dev herda o mesmo processo e as mesmas restrições. Extensões bloqueantes (qualidade, segurança) continuam valendo para ele.

### Fluxo típico de uma melhoria

```text
1. git clone + Using AI-DLC, quero adicionar [feature]...
2. Brownfield detectado → Reverse Engineering
3. Inception (requisitos + impacto no código existente)
4. Workflow Planning → aprovação
5. Code Generation → aprovação
6. Build and Test → pytest deve continuar verde
```

A diferença em relação ao ciclo inicial: há sistema existente a respeitar — **risco e impacto** ganham mais peso.

### Armadilhas (disciplina humana)

Duas condições para a promessa se cumprir:

**1. Versionar os artefatos no Git**

Toda a continuidade depende de commitar:

```text
aidlc-docs/              # Histórico de decisões
.cursor/rules/           # Núcleo do workflow
.aidlc-rule-details/     # Regras + extensões
```

Sem isso, o clone traz só código — o agente começa **cego** sobre decisões passadas. **Este repositório já segue essa prática** (commits incluem `aidlc-docs/`).

**2. Manter documentação alinhada ao código**

Se alguém alterar código **fora** do AI-DLC (edição manual sem atualizar `aidlc-docs/`), o `requirements.md` pode ficar desatualizado. O reverse engineering ainda lê o código real, mas o *porquê* documentado pode mentir.

**Disciplina do time:** mudanças significativas passam pelo fluxo — documentação e código andam juntos.

### Variação entre modelos e IDEs

O AI-DLC busca **reprodutibilidade** — regras claras para resultados parecidos. Porém modelos e IDEs diferentes (Cursor vs Claude Code, modelo A vs B) podem variar um pouco na execução.

| Para máxima consistência | Recomendação |
|--------------------------|--------------|
| Regras | Mesmas em todo o repo (já versionadas) |
| Ferramenta | Padronizar IDE quando possível |
| Modelo | Alinhar modelo principal do time |

As regras **minimizam** a variância; não a eliminam por completo.

### Resumo

O AI-DLC foi desenhado para colaboração: **brownfield + artefatos versionados + regras compartilhadas** fazem o próximo dev começar com contexto, não do zero.

A ferramenta dá o mecanismo; o time mantém o hábito de **commitar `aidlc-docs/`** e **passar mudanças relevantes pelo fluxo**.

---

## Riscos, custos e limitações (leia antes de escalar)

O AI-DLC é poderoso, mas não é mágica. Estes são os pontos que mais causam dor — e como se defender.

### Custo e desperdício

O AI-DLC consome **mais tokens** por rodar várias fases — veja [Custo de tokens](#custo-de-tokens). O desperdício silencioso é outro problema:

| Armadilha | Consequência |
|-----------|--------------|
| Fluxo completo em tarefa trivial | Overhead sem retorno |
| Aprovar gates no automático | Paga o processo **sem** colher o controle |

**Regra prática:** se você não vai **ler e revisar** cada gate de verdade, talvez aquela tarefa não devesse usar AI-DLC. O custo só se paga quando a revisão humana acontece.

### Confiança cega nos artefatos

`requirements.md`, `execution-plan.md` e afins parecem oficiais e completos — mas foram gerados por IA e podem conter **suposições erradas que parecem corretas**.

O risco é baixar a guarda porque *"está documentado e bonito"*. **Documentação confiante ≠ documentação correta.** Trate cada artefato como **proposta a validar**, não como verdade.

### Deriva entre documento e código (drift)

Se alguém edita código na mão **sem** passar pelo fluxo, `aidlc-docs/` passa a descrever um sistema que não existe mais. Isso é **pior que não ter documentação** — engana.

**Defesa cultural:** mudanças significativas passam pelo fluxo, **ou** os docs são explicitamente atualizados.

### Segurança e a pegadinha das extensões

As extensões de segurança incluídas (ex.: Security Baseline) são **referência direcional**, não proteção pronta para produção. Cada organização deve **construir, customizar e testar** suas próprias regras antes de usar em produção.

| Erro perigoso | Realidade |
|---------------|-----------|
| *"Ativei Security Baseline"* | *"Tenho um ponto de partida a endurecer"* |
| *"Meu sistema está seguro"* | *"Preciso validar regras no meu contexto"* |

Confundir extensão ativada com sistema seguro é um erro grave.

### Limites técnicos práticos

| Tópico | Orientação |
|--------|------------|
| **Windows** | Use `/` nos caminhos dentro de arquivos markdown — `\` pode quebrar referências das regras |
| **Tamanho de regras** | No Cursor, regras muito grandes (> ~500 linhas) podem não ser aplicadas bem — prefira regras focadas |
| **Recarregamento** | Após editar qualquer regra, abra um **chat novo** — mudanças não pegam na sessão atual |

### Variabilidade entre modelos e ferramentas

O AI-DLC busca reprodutibilidade, mas **modelos diferentes se comportam diferente**. O mesmo prompt pode gerar resultados distintos entre execuções — é IA, não um compilador.

Para consistência real: padronize **regras + ferramenta + modelo** no time. Não assuma determinismo total.

### O risco humano mais sério: complacência

O processo dá uma sensação tão boa de controle que existe o risco de clicar `✅ Approve` em cada gate **sem ler** — *"o processo cuida disso"*.

Aí você tem **teatro de controle** sem controle. A metodologia move a responsabilidade para você de forma explícita; **não a elimina**.

### Maturidade do projeto

O AI-DLC é um projeto em **evolução ativa** (AWS Labs). Implicações práticas:

- **Operations** ainda é placeholder — não espere deploy/infra automatizados hoje
- Releases podem mudar comportamento — acompanhe atualizações em `aidlc-rules/VERSION` e no repositório upstream
- Ao atualizar regras, **revise suas customizações** em `extensions/`

É algo que evolui rápido (bom), mas pode mudar debaixo de você (exige atenção).

### Alerta em uma frase

> O maior risco do AI-DLC não é técnico — é **humano**: confiar demais nos documentos, tratar aprovação como formalidade, achar que extensão de segurança = sistema seguro.

A ferramenta entrega controle **se você exercer controle de verdade** em cada ponto. Com atenção, é um multiplicador excelente; no automático, vira burocracia cara que mascara os mesmos riscos de sempre.

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
