# Build Instructions

## Prerequisites

| Item | Requirement |
|------|-------------|
| **Python** | 3.11+ (testado com 3.13) |
| **Build Tool** | pip |
| **Dependencies** | `requirements.txt` |
| **SO** | Windows, Linux ou macOS |
| **Memória** | Mínimo 512 MB livres |

## Environment Variables

| Variável | Padrão | Descrição |
|----------|--------|-----------|
| `DATABASE_URL` | `sqlite:///./tasks.db` | URL de conexão SQLite |

## Build Steps

### 1. Criar ambiente virtual (recomendado)

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

### 2. Instalar dependências

```bash
pip install -r requirements.txt
```

### 3. Verificar instalação

```bash
python -c "from app.main import app; print(app.title)"
```

**Saída esperada:** `Task Manager API`

### 4. Inicializar banco (automático no startup)

O banco SQLite é criado automaticamente quando a API inicia (`init_db()` no lifespan).

Para executar a API:

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 5. Verificar build

| Verificação | Como validar |
|-------------|--------------|
| API online | `GET http://localhost:8000/docs` retorna Swagger UI |
| Health implícito | `GET http://localhost:8000/openapi.json` retorna schema |

## Build Artifacts

Este projeto Python não gera binários compilados. Artefatos de runtime:

| Artefato | Local |
|----------|-------|
| Código da aplicação | `app/` |
| Banco SQLite (dev) | `tasks.db` (criado no primeiro run) |
| Cache pytest | `.pytest_cache/` (gerado nos testes) |

## Troubleshooting

### Erro: `ModuleNotFoundError: No module named 'app'`

- **Causa**: Comandos executados fora da raiz do projeto
- **Solução**: `cd` para a raiz (`c:\welligton-ia-dlc`) antes de rodar uvicorn/pytest

### Erro: dependências incompatíveis no ambiente global

- **Causa**: Conflitos com pacotes já instalados no sistema
- **Solução**: Usar `.venv` isolado e `pip install -r requirements.txt` dentro dele

### Erro: `sqlite3.OperationalError: unable to open database file`

- **Causa**: `DATABASE_URL` aponta para diretório inexistente ou sem permissão
- **Solução**: Usar `sqlite:///./tasks.db` ou ajustar caminho com permissão de escrita
