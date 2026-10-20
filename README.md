# 💸 Billing API - Sistema de Faturamento

![Version](https://img.shields.io/badge/version-1.0.1-blue.svg)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat&logo=fastapi)
![GitFlow](https://img.shields.io/badge/GitFlow-Practices-orange)

Uma API RESTful desenvolvida em Python para gerenciamento de clientes e processamento de faturas. 

Este projeto foi construído especificamente para aplicar e demonstrar o domínio do **ciclo de vida de desenvolvimento de software utilizando GitFlow**, simulando um ambiente corporativo real com criação de features, releases e correção de bugs em produção (hotfixes).

## 🚀 Funcionalidades

- **Gestão de Clientes:** Cadastro e listagem de clientes (com validação de documento).
- **Faturamento:** Geração de faturas atreladas aos clientes.
- **Validação de Regra de Negócio:** Bloqueio automático de faturas com valores negativos ou zerados.

## 🛠️ Tecnologias Utilizadas

- **[FastAPI](https://fastapi.tiangolo.com/):** Framework web moderno e de alta performance.
- **[Uvicorn](https://www.uvicorn.org/):** Servidor ASGI leve e rápido.
- **[SQLAlchemy](https://www.sqlalchemy.org/):** ORM para comunicação e modelagem do banco de dados.
- **[Pydantic](https://docs.pydantic.dev/):** Validação de dados e serialização.
- **SQLite:** Banco de dados relacional leve para desenvolvimento.

## 🌿 Arquitetura de Branches (GitFlow)

O histórico de commits deste repositório reflete as melhores práticas de versionamento. As seguintes ramificações foram utilizadas:

- `main`: Código em produção, sempre estável e espelhando as versões lançadas (Tags: `v1.0.0`, `v1.0.1`).
- `develop`: Ramo principal de integração onde as novas funcionalidades são testadas.
- `feature/*`: Branches temporárias para o desenvolvimento de novos módulos (ex: `feature/cadastro-clientes`).
- `release/*`: Preparação e polimento para o lançamento de uma nova versão.
- `hotfix/*`: Ramificações de emergência criadas a partir da `main` para corrigir bugs críticos em produção (ex: `hotfix/bloqueio-fatura-negativa`).

## ⚙️ Como Executar Localmente

### Pré-requisitos
- Python 3.10 ou superior.
- Git.

### Passo a Passo

1. Clone o repositório:
```bash
git clone [https://github.com/SEU_USUARIO/fastapi-billing-api.git](https://github.com/SEU_USUARIO/fastapi-billing-api.git)
cd fastapi-billing-api

```

2. Crie e ative um ambiente virtual:

```bash
# Linux/macOS
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate

```

3. Instale as dependências:

```bash
pip install -r requirements.txt

```

4. Inicie o servidor local:

```bash
uvicorn main:app --reload

```

5. Acesse a documentação interativa (Swagger UI) gerada automaticamente pelo FastAPI:
👉 **[http://127.0.0.1:8000/docs](https://www.google.com/search?q=http://127.0.0.1:8000/docs)**

## 📚 Endpoints Principais

| Método | Rota | Descrição |
| --- | --- | --- |
| `GET` | `/` | Retorna o status de saúde da API. |
| `POST` | `/clientes` | Cria um novo cliente recebendo `nome` e `documento`. |
| `POST` | `/faturas` | Gera uma fatura recebendo `cliente_id`, `valor` e `descricao`. |

---

*Desenvolvido para fins de estudo e composição de portfólio.*
