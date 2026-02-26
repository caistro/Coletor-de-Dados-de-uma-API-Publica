### Clonar o repositório
``git clone https://github.com/caistro/Coletor-de-dados-API-GitHub.git``
``cd Coletor-de-dados-API-GitHub``

---

### Criar ambiente virtual
``python3 -m venv venv``

---

### Ativar ambiente virtual
Linux ou Mac: ``source venv/bin/activate``

Windows: ``venv/scripts/activate``

---

### Instalar dependências
``pip install -r requirements.txt``

---

### Executar o projeto
``python3 -m github_report.main --username torvalds``

### Arquivos gerados
Os arquivos são salvos no diretório ./output/

repos_usuario.json: Resumo dos repositórios do usuário

report_usuario.json: Relatório com métricas dos repositórios do usuário


