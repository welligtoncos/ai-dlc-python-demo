# Requirements Clarification Questions

Por favor, responda às perguntas abaixo preenchendo a tag `[Answer]:` de cada uma.
Use a letra da opção escolhida (ex.: `A`) ou descreva após `X)` quando escolher "Other".

---

## Question 1
Qual nível de rigor na validação de e-mail você deseja?

A) Validação simples — regex básico (parte local + `@` + domínio com TLD), adequado para a maioria dos formulários

B) Validação moderada — regras mais completas (comprimento, caracteres permitidos, domínio com pelo menos um ponto)

C) Validação estrita — aproximação do RFC 5322 (mais complexa, cobre casos raros)

X) Other (please describe after [Answer]: tag below)

[Answer]:

---

## Question 2
Qual deve ser o comportamento da função quando o e-mail é inválido?

A) Retornar `False` (e `True` quando válido) — assinatura `is_valid_email(email: str) -> bool`

B) Retornar `None` para inválido e o e-mail normalizado (strip/lower) quando válido

C) Lançar exceção customizada para e-mail inválido

X) Other (please describe after [Answer]: tag below)

[Answer]:

---

## Question 3
Qual estrutura de projeto Python você prefere?

A) Módulo simples na raiz — `email_validator.py` + `tests/test_email_validator.py`

B) Pacote Python — `src/email_validator/` com `__init__.py` e testes em `tests/`

C) Pacote com `pyproject.toml` (pytest configurado, pronto para distribuição)

X) Other (please describe after [Answer]: tag below)

[Answer]:

---

## Question 4
Qual framework de testes unitários?

A) `pytest` (recomendado)

B) `unittest` (stdlib)

X) Other (please describe after [Answer]: tag below)

[Answer]:

---

## Question 5
A função deve normalizar o e-mail antes de validar (ex.: `strip()`, lowercase no domínio)?

A) Sim — remover espaços e normalizar domínio para minúsculas

B) Não — validar exatamente a string recebida, sem alteração

X) Other (please describe after [Answer]: tag below)

[Answer]:

---

## Question 6 — Security Extensions
Should security extension rules be enforced for this project?

A) Yes — enforce all SECURITY rules as blocking constraints (recommended for production-grade applications)

B) No — skip all SECURITY rules (suitable for PoCs, prototypes, and experimental projects)

X) Other (please describe after [Answer]: tag below)

[Answer]:

---

## Question 7 — Resiliency Extensions
Should the resiliency baseline be applied to this project?

A) Yes — apply the resiliency baseline as directional best practices and design-time guidance

B) No — skip the resiliency baseline (suitable for PoCs, prototypes, and experimental projects)

X) Other (please describe after [Answer]: tag below)

[Answer]:

---

## Question 8 — Property-Based Testing Extension
Should property-based testing (PBT) rules be enforced for this project?

A) Yes — enforce all PBT rules as blocking constraints

B) Partial — enforce PBT rules only for pure functions and serialization round-trips

C) No — skip all PBT rules (suitable for simple CRUD applications, UI-only projects, or thin integration layers)

X) Other (please describe after [Answer]: tag below)

[Answer]:
