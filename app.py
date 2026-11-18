import pandas as pd
import streamlit as st
import plotly.express as px
df = pd.read_csv("numero_veiculos.csv")
cidade = df[df["id_municipio_nome"] == "Betim"]
cidade = cidade[cidade["ano"] == 2025]
cidade = cidade[cidade["mes"] == 12]
cidade = cidade[cidade["quantidade"] > 0]
tabela = cidade[["tipo_veiculo", "quantidade"]]

st.title("Veículos da cidade dos outros")
st.write("Fonte: https://basedosdados.org/")
escolha = st.sidebar.radio(
    "O que você quer ver?",
    ["Tabela", "Gráfico"]
)
if escolha == "Tabela":
    st.header("Tabela")
    st.dataframe(tabela)
else:
    st.header("Gráfico de pizza")
    grafico = px.pie(tabela, names="tipo_veiculo", values="quantidade")
    st.plotly_chart(grafico)