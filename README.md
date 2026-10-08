# 📊 Automação de Relatórios de Vendas

Projeto desenvolvido em **Python** para automatizar a leitura, análise e geração de relatórios de vendas a partir de uma planilha Excel.

A aplicação processa os dados, calcula indicadores, identifica vendas relevantes e gera automaticamente um novo relatório Excel com informações organizadas e visualizações.

---

## 🚀 Tecnologias utilizadas

* 🐍 **Python**
* 🐼 **Pandas**
* 📊 **OpenPyXL**
* 📗 **Excel**
* 🔧 **Git/GitHub**

---

## ⚙️ Funcionalidades

O sistema realiza automaticamente:

* 📥 Leitura de dados de uma planilha Excel
* 🧮 Cálculo do valor total de cada venda
* 💰 Cálculo do faturamento total
* 📊 Cálculo da média por venda
* 📦 Cálculo da quantidade total de produtos
* 🏆 Identificação da maior venda
* ⚠️ Classificação das vendas como `Normal` ou `Atenção`
* 📄 Geração automática de um novo relatório Excel
* 📈 Criação de gráfico de vendas por vendedor
* 🎨 Formatação e organização automática das planilhas

---

## 📋 Exemplo dos resultados

Com os dados utilizados no projeto, a aplicação gera os seguintes indicadores:

| Indicador                       |        Resultado |
| ------------------------------- | ---------------: |
| 💰 Faturamento total            | **R$ 31.200,00** |
| 📊 Média por venda              |  **R$ 6.240,00** |
| 📦 Quantidade total de produtos |           **35** |
| 🏆 Maior venda                  | **R$ 13.500,00** |
| ⚠️ Vendas em atenção            |            **2** |

A maior venda identificada foi realizada pela vendedora **Ana**, com a venda de **3 notebooks**, totalizando **R$ 13.500,00**.

---

## 📁 Estrutura do projeto

```text
automacao-relatorios/
│
├── dados/
│   └── controle_vendas.xlsx
│
├── relatorios/
│   └── relatorio_vendas.xlsx
│
├── src/
│   └── main.py
│
├── .gitignore
└── README.md
```

---

## ▶️ Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/Josiani1111/automacao-relatorios.git
```

### 2. Acesse a pasta do projeto

```bash
cd automacao-relatorios
```

### 3. Crie o ambiente virtual

```bash
python -m venv .venv
```

### 4. Ative o ambiente virtual no Windows

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Instale as dependências

```bash
pip install pandas openpyxl
```

### 6. Execute a aplicação

```bash
python src\main.py
```

Após a execução, o relatório será gerado automaticamente na pasta:

```text
relatorios/
```

---

## 💡 O que este projeto demonstra

Este projeto demonstra conhecimentos práticos em:

* Manipulação e análise de dados com **Pandas**
* Leitura e geração de arquivos Excel
* Automação de tarefas
* Cálculo de indicadores
* Tratamento e organização de dados
* Geração de relatórios
* Criação de gráficos com **OpenPyXL**
* Estruturação de projetos Python
* Git e GitHub

---

## 🎯 Objetivo do projeto

O objetivo deste projeto foi desenvolver uma solução prática de **automação de relatórios**, reduzindo tarefas manuais de análise e organização de dados.

O projeto faz parte do meu portfólio profissional e demonstra minha evolução em **Python, análise de dados e automação de processos**.

---

## 👩‍💻 Sobre mim

Sou **estudante do último ano de Análise e Desenvolvimento de Sistemas** e estou construindo minha carreira na área de Tecnologia.

Busco uma oportunidade como **Desenvolvedora Júnior**, especialmente em posições relacionadas a **Python, backend, APIs REST, automação e desenvolvimento de sistemas**.

Tenho experiência profissional e experiência prática em TI, com perfil analítico, organização e foco na resolução de problemas.

---

⭐ Obrigada por visitar o projeto!
