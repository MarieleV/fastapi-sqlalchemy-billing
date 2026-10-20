<div align="center">
  <!-- Ícone representativo de Faturamento/API -->
  <img src="https://img.icons8.com/fluency/96/000000/invoice.png" alt="Ícone de Faturamento" width="80"/>
  
  <h1>Billing API: Faturamento & GitFlow</h1>

  <p>
    <img src="https://img.shields.io/badge/version-1.0.1-blue.svg?style=for-the-badge" alt="Version">
    <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
    <img src="https://img.shields.io/badge/FastAPI-API_REST-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI">
    <img src="https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite">
    <img src="https://img.shields.io/badge/GitFlow-Practices-FF4F00?style=for-the-badge&logo=git&logoColor=white" alt="GitFlow">
  </p>

  <p><em>API RESTful estruturada para gerenciamento financeiro e demonstração prática do ciclo de vida de software corporativo.</em></p>
</div>

<br>

<h2>Descritivo:</h2>
<p>
  Este projeto consiste em uma <b>API RESTful</b> desenvolvida em Python para gerenciamento de clientes e processamento de faturas. Ele foi construído especificamente para aplicar e demonstrar o domínio de versionamento de código utilizando <b>GitFlow</b>.
</p>
<p>
  A aplicação simula um ambiente corporativo real. Todo o desenvolvimento foi fragmentado metodicamente entre criação de <i>features</i> (módulos de cadastro e faturamento), preparação de <i>releases</i> e a aplicação de <i>hotfixes</i> para correção de bugs mapeados diretamente em produção, garantindo estabilidade na branch principal.
</p>

<br>

<h2> Principais Funcionalidades</h2>

<table>
  <tr>
    <td width="200"><b>Gestão de Clientes</b></td>
    <td>Cadastro e listagem de clientes na base de dados, garantindo a validação e a unicidade de documentos (CPF/CNPJ).</td>
  </tr>
  <tr>
    <td><b>Faturamento</b></td>
    <td>Geração ágil de faturas atreladas via chave estrangeira (Foreign Key) aos clientes previamente cadastrados.</td>
  </tr>
  <tr>
    <td><b>Regras de Negócio</b></td>
    <td>Bloqueio automático e validação estrita com Pydantic para impedir a criação de faturas com valores negativos ou zerados.</td>
  </tr>
  <tr>
    <td><b>Integração com ORM</b></td>
    <td>Comunicação assíncrona com o banco de dados relacional SQLite utilizando SQLAlchemy, garantindo integridade das transações.</td>
  </tr>
</table>

<br>

<h2>🌿 Arquitetura de Branches (GitFlow)</h2>

<p>O histórico de commits deste repositório reflete rigorosamente as melhores práticas de versionamento:</p>

<table>
  <tr>
    <td width="150"><code>main</code></td>
    <td>Código em produção, sempre estável e espelhando as versões lançadas (Tags: <b>v1.0.0</b>, <b>v1.0.1</b>).</td>
  </tr>
  <tr>
    <td><code>develop</code></td>
    <td>Ramo principal de integração onde as novas funcionalidades se encontram e são testadas.</td>
  </tr>
  <tr>
    <td><code>feature/*</code></td>
    <td>Branches ramificadas a partir da <i>develop</i> para desenvolvimento de novos módulos isolados.</td>
  </tr>
  <tr>
    <td><code>release/*</code></td>
    <td>Preparação, documentação e polimento do código para o lançamento de uma nova versão.</td>
  </tr>
  <tr>
    <td><code>hotfix/*</code></td>
    <td>Ramificações de emergência criadas a partir da <i>main</i> para corrigir bugs críticos em produção.</td>
  </tr>
</table>

<br>

<h2>📂 Arquitetura do Sistema</h2>

<details>
  <summary><b>Clique para visualizar a estrutura do projeto</b></summary>
  <br>
  
  ```text
  ├── main.py               # Rotas FastAPI e inicialização do servidor Uvicorn
  ├── models.py             # Modelagem das tabelas do banco (SQLAlchemy)
  ├── schemas.py            # Validação de dados de entrada e saída (Pydantic)
  ├── database.py           # Configuração de conexão e sessão do SQLite
  ├── billing.db            # Banco de dados SQLite (gerado automaticamente)
  ├── .gitignore            # Arquivos ignorados pelo Git (venv, caches, db)
  ├── requirements.txt      # Mapeamento de dependências
  └── README.md             # Documentação do projeto
