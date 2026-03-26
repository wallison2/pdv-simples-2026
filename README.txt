# 🧾 Sistema PDV - Controle Comercial Completo

Sistema PDV (Ponto de Venda) desenvolvido em Python com foco em controle de vendas, estoque e financeiro, oferecendo uma solução completa para pequenos e médios comércios.

---

## 🚀 Funcionalidades

### 🛒 PDV (Ponto de Venda)

* Registro de vendas em tempo real
* Adição de produtos por código ou código de barras
* Cálculo automático de total
* Inclusão de valores avulsos
* Finalização de venda com múltiplas formas de pagamento
* Impressão de cupom

---

### 📦 Controle de Estoque

* Cadastro, edição e exclusão de produtos
* Controle de quantidade em estoque
* Atualização automática após vendas
* Consulta de produtos via API

---

### 💰 Financeiro

* Controle de entradas e saídas
* Abertura e fechamento de caixa
* Relatórios de vendas
* Exportação para Excel

---

### 👥 Usuários e Segurança

* Sistema de login com níveis de acesso (Admin, Gerente, Comum)
* Controle de permissões por perfil
* Limite de tentativas de login

---

### 🔐 Licenciamento

* Sistema de ativação por chave
* Controle de dias restantes de uso
* Validação segura com HMAC

---

### 🏢 Configurações da Empresa

* Cadastro de dados da empresa (CNPJ, endereço, etc)
* Personalização de cupom
* Upload de logo

---

### 🌐 API Integrada

* API própria para:

  * Estoque
  * Usuários
  * Financeiro
* Comunicação via requisições HTTP (REST)

---

## 🛠️ Tecnologias Utilizadas

* Python
* PySide6 (Interface gráfica)
* SQLite (Banco de dados)
* Flask / FastAPI (API backend)
* Requests (integração API)
* Pandas / Matplotlib (relatórios)
* OpenPyXL (exportação Excel)
* ReportLab (geração de PDF)

---

## 📂 Estrutura do Projeto

```
Meu_Sistema/
│
├── main.py
├── api_server.py
├── bd/
│   ├── bdestoque.db
│   ├── bduser.db
│   └── transacoes_entrada_saida.db
└── requirements.txt
```

---

## ⚙️ Como executar

### ▶️ Rodar o sistema

```bash
python main.py
```

---

### 📦 Gerar executável

Com terminal (aparece CMD):

```bash
pyinstaller --onefile --icon="W_W-icone.ico" main.py
```

Sem terminal:

```bash
pyinstaller --onefile --windowed --icon="W_W-icone.ico" main.py
```

---

## 🎯 Objetivo do Projeto

Este sistema foi desenvolvido com foco em resolver problemas reais de gestão comercial, permitindo controle completo de vendas, estoque e financeiro de forma simples e eficiente.

---

## 👨‍💻 Autor

Desenvolvido por **Wallison Nogueira**
