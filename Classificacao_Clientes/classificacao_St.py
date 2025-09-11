"""
Script: dashboard_clientes.py
Objetivo: Criar um dashboard interativo em Streamlit para analisar clientes,
          aplicar classificação, visualizar gráficos e testar cenários.

Como usar:
1. Substitua os dados fictícios pela sua base (ou permita upload de CSV/Excel).
2. Execute: streamlit run dashboard_clientes.py
3. Acesse no navegador: http://localhost:8501
"""

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# ======================
# Upload da base
# ======================
st.title("📊 Dashboard de Segmentação de Clientes")

uploaded_file = st.file_uploader("Carregar arquivo Excel/CSV", type=["csv","xlsx"])
if uploaded_file:
    if uploaded_file.name.endswith("csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)
else:
    st.warning("Carregando dados fictícios...")
    df = pd.DataFrame({
        "Cliente": ["Cliente A", "Cliente B", "Cliente C"],
        "Faturamento": [500000, 200000, 150000],
        "Frequencia": [25, 10, 8],
        "Mix_Compras": [10, 7, 5],
        "Margem_Lucro": [0.25, 0.20, 0.18],
        "Ticket_Medio": [20000, 20000, 18750],
        "Tempo_Relacionamento": [5, 3, 2],
        "Risco_Inadimplencia": [1, 2, 3],
        "Custo_Atendimento": [2, 3, 4],
        "Engajamento": [9, 7, 5],
        "Sazonalidade": [8, 6, 5]
    })

# ======================
# Pesos dos critérios
# ======================
pesos = {
    "Faturamento": 0.15,
    "Frequencia": 0.15,
    "Mix_Compras": 0.10,
    "Margem_Lucro": 0.20,
    "Ticket_Medio": 0.08,
    "Tempo_Relacionamento": 0.10,
    "Risco_Inadimplencia": -0.02,
    "Custo_Atendimento": -0.04,
    "Engajamento": 0.10,
    "Sazonalidade": 0.06
}

# Normalização
for col in pesos.keys():
    if col in ["Risco_Inadimplencia", "Custo_Atendimento"]:
        df[col+"_Score"] = 10 - (df[col]-df[col].min())/(df[col].max()-df[col].min())*10
    else:
        df[col+"_Score"] = (df[col]-df[col].min())/(df[col].max()-df[col].min())*10

df["Score_Final"] = sum(df[col+"_Score"]*peso for col, peso in pesos.items())

def classificar(score):
    if score >= 8: return "Classe A"
    elif score >= 6: return "Classe B"
    elif score >= 4: return "Classe C"
    else: return "Classe D"

df["Classe"] = df["Score_Final"].apply(classificar)

# ======================
# Exibição no dashboard
# ======================
st.subheader("📋 Tabela de Clientes")
st.dataframe(df)

st.subheader("📊 Distribuição por Classe")
fig, ax = plt.subplots()
df["Classe"].value_counts().plot.pie(autopct="%.1f%%", ax=ax)
st.pyplot(fig)

st.subheader("🏆 Ranking TOP 10 Clientes")
top10 = df.nlargest(10, "Score_Final")[["Cliente","Score_Final","Classe"]]
st.table(top10)

st.subheader("🔮 Simulação de Cenários")
fator = st.slider("Ajustar crescimento (%)", -20, 20, 0)
df["Score_Simulado"] = df["Score_Final"] * (1 + fator/100)
st.dataframe(df[["Cliente","Score_Final","Score_Simulado","Classe"]])
