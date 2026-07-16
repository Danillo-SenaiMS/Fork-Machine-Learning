# Machine Learning - Documentação do Projeto

## Visão Geral

Repositório de estudos e práticas em Machine Learning, com foco em **classificação supervisionada** usando Árvores de Decisão e sistemas de scoring para segmentação de clientes.

---

## Estrutura do Projeto

```
├── data/                    # Bases de dados
│   ├── dados_frutas.xlsx          # Case 01 - Classificação de frutas
│   ├── dados_cerveja.xlsx         # Case 02 - Classificação de cervejas
│   ├── dados_clones.parquet       # Case 03 - Classificação de clones (Star Wars)
│   ├── advertising.csv            # Dados de publicidade
│   ├── ecommerce-customers.csv    # Dados de e-commerce
│   └── dados_cerveja_nota.xlsx    # Variação do case 02
├── python/                  # Scripts principais
│   ├── case01.py                  # Árvore de decisão - Frutas
│   ├── case02.py                  # Árvore de decisão - Cervejas
│   ├── case03.py                  # Árvore de decisão - Clones (Star Wars)
│   ├── classificacao.py           # Scoring de clientes (Excel)
│   ├── classificacao_St.py        # Dashboard Streamlit interativo
│   └── 01_classificação.py        # Script auxiliar
├── notebook/
│   └── 01_classificacao.ipynb     # Jupyter notebook - MNIST
├── docs/
│   └── Apostila - Modelos de Classificacao e Regressao.pdf
├── requirements.txt               # Dependências do projeto
└── requeriments.txt               # Dependências (cópia)
```

---

## Casos de Estudo

### Case 01 - Classificação de Frutas (`case01.py`)
- **Objetivo:** Classificar frutas com base em características (arredondada, suculenta, vermelha, doce)
- **Método:** Árvore de Decisão (scikit-learn)
- **Dados:** `data/dados_frutas.xlsx`

### Case 02 - Classificação de Cervejas (`case02.py`)
- **Objetivo:** Classificar tipos de cerveja (clara/escura) por características (temperatura, copo, espuma, cor)
- **Método:** Árvore de Decisão com conversão de variáveis categóricas para numéricas
- **Dados:** `data/dados_cerveja.xlsx`

### Case 03 - Classificação de Clones (`case03.py`)
- **Objetivo:** Classificar status de clones com base em massa e estatura
- **Método:** Árvore de Decisão com análise de importância das features
- **Dados:** `data/dados_clones.parquet`

### Classificação de Clientes (`classificacao.py` e `classificacao_St.py`)
- **Objetivo:** Segmentar clientes em classes (A, B, C, D) usando sistema de scoring ponderado
- **Método:** Normalização Min-Max, cálculo de score final, classificação por faixas
- **Dashboard:** Interface interativa em Streamlit com upload de dados, gráficos e simulação de cenários
- **Métricas:** Faturamento, frequência, mix de compras, margem de lucro, ticket médio, tempo de relacionamento, risco de inadimplência, custo de atendimento, engajamento e sazonalidade

### MNIST (`notebook/01_classificacao.ipynb`)
- **Objetivo:** Explorar o dataset MNIST para classificação de dígitos manuscritos
- **Método:** Análise exploratória com visualização de imagens

---

## Dependências Principais

- **scikit-learn** - Modelos de Machine Learning
- **pandas** - Manipulação de dados
- **matplotlib** / **seaborn** - Visualização
- **streamlit** - Dashboard interativo
- **numpy** - Computação numérica
- **plotly** - Gráficos interativos

---

## Como Executar

### Scripts Python
```bash
python python/case01.py
python python/case02.py
python python/case03.py
```

### Dashboard Streamlit
```bash
streamlit run python/classificacao_St.py
```
Acesse: http://localhost:8501

### Instalar dependências
```bash
pip install -r requirements.txt
```
