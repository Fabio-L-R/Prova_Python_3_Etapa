import pandas as pd
import streamlit as st
import plotly.express as px

st.title("Prova Python")

df = pd.read_csv("bd_iqvu_1994_2016.csv", sep=";", encoding="latin-1",
decimal=",")
df.columns = df.columns.str.replace("\ufeff", "", regex=False).str.strip()

#---------------------------------------------------------

st.header("Passo 1")

df_filtrado = df[
    (df["NOMEUP"].isin(["Taquaril", "Santa Ines"])) &
    (df["ï»¿SERIE"] == "SERIE HISTORICA")
]

st.dataframe(df_filtrado)

#---------------------------------------------------------

st.header("Passo 2")

st.sidebar.header("Tabela / Gráficos")

barra_lateral = st.sidebar.selectbox("Escolha", ["Tabela", "Gráficos"])

df_taquaril = df[df["NOMEUP"] == "Taquaril"]

fig_linha_taquaril = px.line(
    df_taquaril,
    x="ANO",
    y="IQVU",
    markers=True,
    title="Gráfico de Linha Taquaril",
    template="plotly_dark"
)

st.plotly_chart(fig_linha_taquaril)

df_santa = df[df["NOMEUP"] == "Santa Ines"]

fig_linha_santa = px.line(
    df_santa,
    x="ANO",
    y="IQVU",
    markers=True,
    title="Gráfico de Linha Santa Inês",
    template="plotly_dark"
)

st.plotly_chart(fig_linha_santa)