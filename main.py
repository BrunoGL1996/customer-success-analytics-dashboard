import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# ============================================================
# CUSTOMER HEALTH SEGMENTATION & CHURN RISK ANALYSIS
# ============================================================

print("\n" + "=" * 60)
print("CUSTOMER HEALTH SEGMENTATION & CHURN RISK ANALYSIS")
print("=" * 60)


# ============================================================
# 1. CONFIGURAÇÃO
# ============================================================

np.random.seed(42)

n = 1000


# ============================================================
# 2. GERAÇÃO DA BASE DE CLIENTES B2B SaaS
# ============================================================

df = pd.DataFrame({

    "customer_id": range(1, n + 1),

    "monthly_revenue": np.random.lognormal(
        mean=7.5,
        sigma=0.6,
        size=n
    ).round(2),

    "months_active": np.random.randint(
        1,
        48,
        n
    ),

    "login_frequency": np.random.poisson(
        12,
        n
    ),

    "product_adoption": np.random.uniform(
        20,
        100,
        n
    ).round(1),

    "support_tickets": np.random.poisson(
        4,
        n
    ),

    "csat": np.random.uniform(
        60,
        100,
        n
    ).round(1),

    "last_login_days": np.random.randint(
        0,
        90,
        n
    ),

    "renewal_days": np.random.randint(
        1,
        365,
        n
    )
})


print("\nBase criada!")
print(f"Total de clientes: {len(df)}")


# ============================================================
# 3. NORMALIZAÇÃO DOS INDICADORES
# ============================================================

def normalize(series):

    return (
        (series - series.min())
        /
        (series.max() - series.min())
        * 100
    )


# Adoção
df["adoption_score"] = df["product_adoption"]


# Engajamento
df["engagement_score"] = normalize(
    df["login_frequency"]
)


# Satisfação
df["csat_score"] = df["csat"]


# Suporte
# Quanto menos tickets, melhor
df["support_score"] = (
    100
    -
    normalize(df["support_tickets"])
)


# Recência
# Quanto menos dias desde o último login, melhor
df["recency_score"] = (
    100
    -
    normalize(df["last_login_days"])
)


# ============================================================
# 4. CUSTOMER HEALTH SCORE
# ============================================================

df["health_score"] = (

    df["adoption_score"] * 0.30

    +

    df["engagement_score"] * 0.25

    +

    df["csat_score"] * 0.20

    +

    df["support_score"] * 0.15

    +

    df["recency_score"] * 0.10

).round(2)


print("\nHealth Score calculado!")

print(
    "\nEstatísticas do Health Score:"
)

print(
    df["health_score"].describe().round(2)
)


# ============================================================
# 5. SEGMENTAÇÃO DE CLIENTES
# ============================================================

def classify_customer(score):

    if score >= 80:

        return "Healthy"

    elif score >= 65:

        return "Growth"

    elif score >= 50:

        return "Attention"

    elif score >= 35:

        return "At Risk"

    else:

        return "Critical"


df["segment"] = df["health_score"].apply(
    classify_customer
)


# ============================================================
# 6. CHURN RISK
# ============================================================

def churn_risk(score):

    if score >= 70:

        return "Low"

    elif score >= 50:

        return "Medium"

    else:

        return "High"


df["churn_risk"] = df["health_score"].apply(
    churn_risk
)


# ============================================================
# 7. PRIORIZAÇÃO DA CARTEIRA
# ============================================================

revenue_median = df[
    "monthly_revenue"
].median()


df["priority"] = np.where(

    (
        df["churn_risk"] == "High"
    )

    &

    (
        df["monthly_revenue"]
        >=
        revenue_median
    ),

    "High Priority",

    "Standard"

)


# ============================================================
# 8. VISÃO GERAL
# ============================================================

print("\n" + "=" * 60)
print("VISÃO GERAL DA CARTEIRA")
print("=" * 60)

print(
    f"\nClientes: {len(df)}"
)

print(
    f"Receita mensal total: "
    f"R$ {df['monthly_revenue'].sum():,.2f}"
)

print(
    f"Health Score médio: "
    f"{df['health_score'].mean():.2f}"
)


# ============================================================
# 9. CLIENTES POR SEGMENTO
# ============================================================

print("\n" + "=" * 60)
print("CLIENTES POR SEGMENTO")
print("=" * 60)

segment_counts = (
    df["segment"]
    .value_counts()
)

print(segment_counts)


print("\nPercentual da carteira:")

segment_percentage = (
    df["segment"]
    .value_counts(
        normalize=True
    )
    * 100
).round(2)

print(segment_percentage)


# ============================================================
# 10. CHURN RISK
# ============================================================

print("\n" + "=" * 60)
print("CHURN RISK")
print("=" * 60)

print(
    df["churn_risk"]
    .value_counts()
)


# ============================================================
# 11. PRIORIDADE
# ============================================================

print("\n" + "=" * 60)
print("PRIORIDADE DE ATUAÇÃO")
print("=" * 60)

print(
    df["priority"]
    .value_counts()
)


# ============================================================
# 12. RESUMO POR SEGMENTO
# ============================================================

segment_summary = df.groupby(
    "segment"
).agg(

    customers=(
        "customer_id",
        "count"
    ),

    total_revenue=(
        "monthly_revenue",
        "sum"
    ),

    avg_revenue=(
        "monthly_revenue",
        "mean"
    ),

    avg_health_score=(
        "health_score",
        "mean"
    ),

    avg_adoption=(
        "product_adoption",
        "mean"
    ),

    avg_login_frequency=(
        "login_frequency",
        "mean"
    ),

    avg_csat=(
        "csat",
        "mean"
    ),

    avg_support_tickets=(
        "support_tickets",
        "mean"
    ),

    avg_last_login_days=(
        "last_login_days",
        "mean"
    )

).round(2)


print("\n" + "=" * 60)
print("RESUMO POR SEGMENTO")
print("=" * 60)

print(
    segment_summary
)


# ============================================================
# 13. CLIENTES EM RISCO
# ============================================================

critical_customers = df[
    df["segment"].isin(
        [
            "At Risk",
            "Critical"
        ]
    )
].sort_values(

    "monthly_revenue",

    ascending=False
)


print("\n" + "=" * 60)
print("TOP CLIENTES EM RISCO")
print("=" * 60)


print(

    critical_customers[
        [
            "customer_id",
            "monthly_revenue",
            "health_score",
            "segment",
            "churn_risk",
            "priority"
        ]
    ].head(15)

)


# ============================================================
# 14. CLIENTES DE ALTA PRIORIDADE
# ============================================================

high_priority = df[
    df["priority"]
    ==
    "High Priority"
].sort_values(

    "monthly_revenue",

    ascending=False
)


print("\n" + "=" * 60)
print("TOP CLIENTES - ALTA PRIORIDADE")
print("=" * 60)


print(

    high_priority[
        [
            "customer_id",
            "monthly_revenue",
            "health_score",
            "segment",
            "churn_risk"
        ]
    ].head(15)

)


# ============================================================
# 15. GRÁFICO 1 - SEGMENTAÇÃO
# ============================================================

plt.figure(
    figsize=(10, 6)
)

segment_counts.plot(
    kind="bar"
)

plt.title(
    "Distribuição de Clientes por Segmento"
)

plt.xlabel(
    "Segmento"
)

plt.ylabel(
    "Quantidade de Clientes"
)

plt.xticks(
    rotation=0
)

plt.tight_layout()

plt.savefig(
    "segment_distribution.png",
    dpi=300
)

plt.show()


# ============================================================
# 16. GRÁFICO 2 - HEALTH SCORE
# ============================================================

plt.figure(
    figsize=(10, 6)
)

plt.hist(
    df["health_score"],
    bins=20
)

plt.title(
    "Distribuição do Customer Health Score"
)

plt.xlabel(
    "Health Score"
)

plt.ylabel(
    "Quantidade de Clientes"
)

plt.tight_layout()

plt.savefig(
    "health_score_distribution.png",
    dpi=300
)

plt.show()


# ============================================================
# 17. GRÁFICO 3 - HEALTH SCORE X RECEITA
# ============================================================

plt.figure(
    figsize=(10, 6)
)

plt.scatter(

    df["health_score"],

    df["monthly_revenue"],

    alpha=0.5

)

plt.title(
    "Customer Health Score x Receita Mensal"
)

plt.xlabel(
    "Health Score"
)

plt.ylabel(
    "Receita Mensal"
)

plt.tight_layout()

plt.savefig(
    "health_vs_revenue.png",
    dpi=300
)

plt.show()


# ============================================================
# 18. EXPORTAÇÃO DOS DADOS
# ============================================================

df.to_csv(
    "customers.csv",
    index=False
)


segment_summary.to_csv(
    "segment_summary.csv"
)


high_priority.to_csv(
    "high_priority_customers.csv",
    index=False
)


print("\n" + "=" * 60)
print("PROJETO FINALIZADO!")
print("=" * 60)

print(
    "\nArquivos gerados:"
)

print(
    "- customers.csv"
)

print(
    "- segment_summary.csv"
)

print(
    "- high_priority_customers.csv"
)

print(
    "- segment_distribution.png"
)

print(
    "- health_score_distribution.png"
)

print(
    "- health_vs_revenue.png"
)

print(
    "\nPróximo passo: Power BI!"
)

# ============================================================
# 18. EXPORTAÇÃO DOS DADOS (FORMATO EXCEL)
# ============================================================

# Exporta a base completa de clientes para Excel
df.to_excel(
    "customers.xlsx",
    index=False
)

# Exporta o resumo por segmento
segment_summary.to_excel(
    "segment_summary.xlsx"
)

# Exporta apenas os clientes de alta prioridade (ótimo para o time de CS agir)
high_priority.to_excel(
    "high_priority_customers.xlsx",
    index=False
)


print("\n" + "=" * 60)
print("PROJETO FINALIZADO!")
print("=" * 60)

print("\nArquivos Excel gerados na pasta do projeto:")
print("- customers.xlsx")
print("- segment_summary.xlsx")
print("- high_priority_customers.xlsx")