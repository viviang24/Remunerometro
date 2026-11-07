# Remunerômetro PB
### Análise de padrões remuneratórios na Paraíba com Aprendizado de Máquina

## 1. Apresentação

O Remunerômetro PB é um projeto acadêmico desenvolvido na disciplina de **Aprendizado de Máquina Supervisionado**.

O trabalho utiliza dados da Relação Anual de Informações Sociais (RAIS) para investigar padrões remuneratórios no estado da Paraíba, explorando características dos vínculos de trabalho e relações entre variáveis disponíveis na base.

A proposta envolve a construção de um fluxo de trabalho que integra preparação e tratamento de dados, análise exploratória, organização dos conjuntos de treinamento e teste, desenvolvimento de modelos preditivos e avaliação de resultados.

## 2. Objetivo geral

Investigar padrões remuneratórios no estado da Paraíba por meio de técnicas de análise de dados e aprendizado de máquina supervisionado, utilizando informações provenientes da RAIS.

## 3. Objetivos específicos

- Preparar e tratar os dados utilizados na análise.
- Delimitar o conjunto de dados referente ao estado da Paraíba.
- Explorar a distribuição das variáveis e suas relações.
- Identificar características relevantes para a investigação dos padrões remuneratórios.
- Organizar os dados para aplicação de técnicas de aprendizado de máquina.
- Desenvolver e avaliar modelos preditivos.
- Analisar os resultados considerando o desempenho dos modelos e as limitações dos dados.

## 4. Fonte de dados

A principal fonte de dados utilizada no projeto é a **Relação Anual de Informações Sociais (RAIS)**, disponibilizada pelo Ministério do Trabalho e Emprego.

A RAIS reúne informações administrativas sobre vínculos formais de trabalho, permitindo análises relacionadas ao mercado de trabalho, às características dos trabalhadores e às remunerações.

Neste projeto, os dados são utilizados com recorte territorial para o estado da Paraíba.

**Observação:** os arquivos brutos e processados não estão armazenados neste repositório. Essa organização evita a publicação de bases de dados extensas e mantém os arquivos de trabalho separados do código-fonte.

## 5. Etapas metodológicas

O desenvolvimento está organizado em etapas:

### 5.1. Preparação dos dados

Leitura dos arquivos de origem, organização das informações e aplicação dos procedimentos necessários para construção da base analítica.

### 5.2. Recorte territorial

Seleção das informações correspondentes ao estado da Paraíba, delimitando a população de interesse para a investigação.

### 5.3. Tratamento e organização

Tratamento das variáveis, adequação dos formatos e organização dos dados para utilização nas etapas seguintes.

### 5.4. Análise exploratória

Investigação das características da base, das distribuições das variáveis e dos padrões identificados nos dados.

### 5.5. Preparação para modelagem

Organização dos conjuntos de dados destinados ao treinamento e à avaliação dos modelos, preservando a separação definida no procedimento experimental.

### 5.6. Modelagem e avaliação

Aplicação de técnicas de aprendizado de máquina supervisionado e análise das métricas de desempenho, considerando as características e limitações do problema investigado.

## 6. Estrutura do repositório

```text
remunerometro/
├── notebook/
│   ├── REM_20240045345_Vivian.ipynb
│   └── REM_20240045345_Vivian.html
├── scripts/
│   ├── preparar_base_pb.py
│   └── separar_dados_Vivian.py
├── requirements.txt
├── .gitignore
└── README.md
```
