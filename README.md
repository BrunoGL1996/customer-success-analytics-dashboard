# Customer Success Analytics Dashboard

Esse projeto começou como um exercício de **segmentação de clientes** durante meus estudos em Customer Analytics e acabou evoluindo para uma análise mais completa de **Customer Health, Churn Risk e MRR**.

A ideia foi trabalhar com uma carteira B2B SaaS simulada e entender como os dados poderiam ajudar um time de Customer Success a identificar quais clientes merecem mais atenção.

## Sobre os dados

A carteira possui:

- 1.000 clientes
- R$ 2,18M em MRR
- 150 clientes classificados como alto risco de churn
- 80 clientes classificados como High Priority
- Health Score médio de 59,44

## Como o projeto foi desenvolvido

O projeto passou por algumas etapas, começando pela exploração dos dados e chegando ao dashboard final.

### 1. Python e Pandas

Primeiro, utilizei Python e Pandas para explorar a base e entender a distribuição dos principais indicadores.

Analisei principalmente:

- Health Score
- CSAT
- MRR
- Churn Risk
- comportamento dos diferentes grupos de clientes

A ideia nessa etapa foi entender melhor a carteira antes de partir para a segmentação.

### 2. Segmentação no Excel

Depois da exploração inicial, levei os dados para o Excel e comecei a trabalhar a segmentação.

Cruzei principalmente **Health Score, Churn Risk e MRR** para tentar responder uma pergunta:

> Se vários clientes estão em risco, quais deles deveriam receber atenção primeiro?

Isso ajudou a separar clientes em diferentes níveis de prioridade, considerando não apenas o risco, mas também o impacto que aquele cliente representa para a carteira.

### 3. Dashboard

Por fim, transformei a análise em um dashboard no Excel.

O dashboard reúne algumas das principais informações da carteira, como:

- relação entre CSAT e Health Score;
- distribuição do MRR;
- risco de churn;
- Health Score por cliente;
- CSAT;
- MRR individual;
- clientes de maior prioridade.

![Dashboard](images/dashboard.png)

## O principal aprendizado

O ponto que mais gostei nesse projeto foi perceber que **risco de churn, sozinho, não conta toda a história**.

Um cliente pode estar em risco, mas outro cliente com um nível de risco semelhante pode representar um impacto muito maior para o negócio.

Ao cruzar **saúde, satisfação, risco e receita**, a análise começa a ficar mais útil para a tomada de decisão do time de CS.

O objetivo não é simplesmente encontrar clientes em risco.

É ajudar a responder:

> **Onde o time deveria concentrar seus esforços primeiro?**

## Ferramentas utilizadas

- Python
- Pandas
- Microsoft Excel

## Estrutura do projeto

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
│   └── dashboard.png
│
└── README.md
```

## Próximos passos

Algumas coisas que eu gostaria de explorar em uma próxima versão:

- criar uma análise preditiva de churn;
- acompanhar a evolução do Health Score ao longo do tempo;
- adicionar análise de cohort;
- testar outros modelos de segmentação;
- transformar o dashboard em uma solução mais automatizada.

---

Projeto desenvolvido como parte dos meus estudos e projetos práticos em **Customer Success, Customer Analytics e CX**.
