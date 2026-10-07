# Automação de Relatórios de Vendas

Projeto desenvolvido em Python para automatizar a leitura, análise e geração de relatórios de vendas a partir de uma planilha Excel.

## Sobre o projeto

A aplicação lê os dados de vendas, calcula automaticamente os valores das vendas, identifica a maior venda, gera indicadores e classifica as vendas de acordo com um valor mínimo definido.

Ao final, o sistema gera um novo arquivo Excel com:

* Resumo dos principais indicadores
* Relatório detalhado das vendas
* Identificação de vendas que precisam de atenção
* Gráfico de vendas por vendedor
* Formatação automática das planilhas

## Tecnologias utilizadas

* Python
* Pandas
* OpenPyXL
* Excel
* Git/GitHub

## Funcionalidades

* Leitura de dados de uma planilha Excel
* Cálculo automático do total de cada venda
* Cálculo do faturamento total
* Cálculo da média por venda
* Cálculo da quantidade total de produtos
* Identificação da maior venda
* Classificação das vendas como `Normal` ou `Atenção`
* Geração automática de relatório Excel
* Criação de gráfico de vendas
* Formatação e organização automática das planilhas

## Estrutura do projeto

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

## Como executar

### 1. Clone o repositório

```bash
git clone URL_DO_REPOSITORIO
```

### 2. Entre na pasta do projeto

```bash
cd automacao-relatorios
```

### 3. Crie e ative o ambiente virtual

No Windows:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 4. Instale as dependências

```bash
pip install pandas openpyxl
```

### 5. Execute o projeto

```bash
python src\main.py
```

O relatório será gerado automaticamente na pasta:

```text
relatorios/
```

## Exemplo dos resultados

Com os dados utilizados no projeto, a aplicação identifica:

* Faturamento total: **R$ 31.200,00**
* Média por venda: **R$ 6.240,00**
* Quantidade total de produtos: **35**
* Maior venda: **R$ 13.500,00**
* Vendas em atenção: **2**

## Objetivo

Este projeto foi desenvolvido como prática de Python e automação de processos, aplicando manipulação de dados, geração de relatórios e organização de informações em Excel.

Também faz parte do meu portfólio de projetos voltados ao desenvolvimento de software e automação.

## Autora

**Josiani Oliveira**

Estudante do último ano de Análise e Desenvolvimento de Sistemas.

Conhecimentos em Python, SQL, APIs REST, Git/GitHub e desenvolvimento de sistemas.
