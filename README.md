# customer-success-analytics-dashboard
Customer Success Analytics project using Python, Pandas and Excel to analyze customer health, churn risk, MRR, segmentation and CS prioritization.
# Customer Success Analytics Dashboard

## 📌 Sobre o projeto

Projeto de **Customer Analytics aplicado a Customer Success**, desenvolvido a partir de uma carteira B2B SaaS simulada com **1.000 clientes**.

O objetivo foi transformar dados de clientes em uma visão estruturada de **Customer Health, Churn Risk, MRR e priorização de atendimento**.

O projeto começou como uma análise de segmentação e evoluiu para um dashboard capaz de apoiar decisões de Customer Success.

---

## 🎯 Objetivo

Responder a uma pergunta simples:

> **Com 1.000 clientes na carteira, quais clientes deveriam receber atenção primeiro?**

Para isso, foram analisados diferentes indicadores de comportamento e valor:

- Health Score
- CSAT
- MRR (Monthly Recurring Revenue)
- Churn Risk
- Segmentação de clientes

A ideia foi não tratar todos os clientes em risco da mesma forma, considerando também o impacto financeiro e a saúde da carteira.

---

## 📊 Dados da carteira

A base simulada contém:

| Indicador | Resultado |
|---|---:|
| Clientes | 1.000 |
| MRR total | R$ 2,18M |
| Clientes em alto risco | 150 |
| Clientes High Priority | 80 |
| Health Score médio | 59,44 |

---

# 🔎 Etapa 1 — Exploração dos dados

A primeira etapa foi entender a estrutura da carteira e identificar os principais indicadores disponíveis.

Foram analisados:

- distribuição de clientes;
- MRR;
- CSAT;
- Health Score;
- risco de churn;
- comportamento dos diferentes segmentos.

Essa etapa foi realizada utilizando **Python e Pandas**.

### Ferramentas

🐍 Python  
🐼 Pandas  
📊 Excel

---

# 🧮 Etapa 2 — Customer Health Score

A partir dos dados disponíveis, foi estruturado um modelo de **Customer Health Score** para representar a situação de cada cliente.

O Health Score foi utilizado como uma das variáveis para entender:

- saúde da carteira;
- clientes potencialmente vulneráveis;
- relação entre satisfação e saúde;
- possíveis sinais de churn.

---

# 🎯 Etapa 3 — Segmentação e priorização

Após analisar os indicadores individualmente, os clientes foram segmentados considerando principalmente:

**Health Score + Churn Risk + MRR**

O objetivo foi diferenciar:

> **“clientes em risco”**

de

> **“clientes em risco que também representam uma prioridade maior para o negócio”.**

Essa etapa permitiu identificar os clientes classificados como **High Priority**.

---

# 📈 Etapa 4 — Dashboard

Depois da análise e segmentação, os dados foram transformados em um dashboard no Excel.

### Principais visualizações

**CSAT × Health Score**

Permite observar a relação entre satisfação e saúde dos clientes.

**Distribuição do MRR**

Mostra como a receita mensal está distribuída entre os segmentos da carteira.

**Customer & Churn Risk**

Tabela com visão individual dos clientes, incluindo:

- Customer ID
- Churn Risk
- Health Score
- CSAT
- MRR

### Dashboard

![Customer Success Analytics Dashboard](images/dashboard.png)

---

# 💡 Principais insights

O principal aprendizado do projeto foi que:

> **Estar em risco de churn não significa necessariamente ter a mesma prioridade.**

Ao cruzar **saúde do cliente, risco e impacto financeiro**, é possível criar uma visão mais estratégica da carteira e direcionar os esforços do time de CS para onde existe maior necessidade ou impacto potencial.

Isso transforma uma análise de dados em uma ferramenta de **priorização operacional**.

---

# 🔄 Fluxo do projeto

```text
Dados
  ↓
Exploração
  ↓
Customer Health Score
  ↓
Análise de Churn Risk
  ↓
Segmentação
  ↓
Priorização
  ↓
Dashboard
  ↓
Decisão de CS
```

---

# 🛠️ Tecnologias utilizadas

- Python
- Pandas
- Microsoft Excel
- Customer Success Analytics
- Customer Health Score
- Customer Segmentation
- Churn Analysis
- Data Visualization

---

# 📁 Estrutura do projeto

```text
customer-success-analytics-dashboard/
│
├── data/
│   └── customer_data.xlsx
│
├── python/
│   └── customer_analysis.ipynb
│
├── excel/
│   └── customer_segmentation.xlsx
│
├── dashboard/
│   └── customer_health_dashboard.xlsx
│
├── images/
│   ├── dashboard.png
│   └── segmentation.png
│
└── README.md
```

---

## 🚀 Próximos passos

Algumas evoluções possíveis para o projeto:

- automatizar a atualização dos indicadores;
- criar um modelo preditivo de churn;
- adicionar análise de cohort;
- acompanhar evolução do Health Score ao longo do tempo;
- integrar os dados com Power BI;
- criar alertas para clientes de alto risco;
- desenvolver uma camada de recomendação de ações para o time de CS.

---

## 👤 Autor

Projeto desenvolvido como parte do meu processo de aprofundamento em **Customer Success, Customer Analytics, CX e Data Analytics**.
