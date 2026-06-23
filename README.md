# ai-dlc-python-demo

Demonstração do workflow **AI-DLC** (AI-Driven Development Life Cycle) com Python: planejamento guiado por IA, documentação rastreável e implementação incremental.

Repositório: [github.com/welligtoncos/ai-dlc-python-demo](https://github.com/welligtoncos/ai-dlc-python-demo)

## Objetivo

Construir uma função utilitária em Python que **valida o formato de e-mail**, acompanhada de **testes unitários** — seguindo as fases do AI-DLC (Inception → Construction → Build & Test).

## Status do projeto

| Fase | Status |
|------|--------|
| Workspace Detection | Concluído |
| Requirements Analysis | Em andamento — [perguntas pendentes](aidlc-docs/inception/requirements/requirement-verification-questions.md) |
| Code Generation | Pendente |
| Build and Test | Pendente |

O código da validação de e-mail ainda **não foi gerado**; o workflow está na fase de requisitos.

## Estrutura do repositório

```text
.
├── README.md                 # Este arquivo
├── .cursor/rules/            # Regra Cursor do workflow AI-DLC
├── .aidlc-rule-details/      # Detalhes das regras AI-DLC (Cursor)
├── aidlc-rules/              # Pacote de regras AI-DLC (referência)
└── aidlc-docs/               # Documentação gerada pelo workflow
    ├── aidlc-state.md        # Estado e progresso do AI-DLC
    ├── audit.md              # Trilha de auditoria
    └── inception/
        └── requirements/     # Requisitos e perguntas de clarificação
```

**Regra de organização:** código de aplicação na raiz do projeto; documentação do AI-DLC apenas em `aidlc-docs/`.

## O que é o AI-DLC?

O AI-DLC é um processo adaptativo de desenvolvimento em que a IA:

- Analisa o workspace e define se o projeto é greenfield ou brownfield
- Coleta requisitos e faz perguntas quando necessário
- Planeja quais etapas executar (simples vs. complexo)
- Gera código, testes e instruções de build
- Mantém auditoria completa das decisões

## Próximos passos

1. Responder as perguntas em [`aidlc-docs/inception/requirements/requirement-verification-questions.md`](aidlc-docs/inception/requirements/requirement-verification-questions.md)
2. Aprovar o documento de requisitos
3. Gerar `email_validator.py` e testes com `pytest`

## Desenvolvimento (após geração do código)

```bash
# Criar ambiente virtual (recomendado)
python -m venv .venv
.venv\Scripts\activate   # Windows
# source .venv/bin/activate  # Linux/macOS

# Instalar dependências de teste
pip install pytest

# Executar testes
pytest
```

## Licença

A definir.

## Autor

[Welligton](https://github.com/welligtoncos)
