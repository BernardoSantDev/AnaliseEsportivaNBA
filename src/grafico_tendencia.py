import streamlit as st

def grafico_tendencia(df, estatistica, ultimos):

    df_recentes = df.head(ultimos).copy()

    df_recentes = df_recentes.sort_values("DATA")

    st.write("📊 Gráfico de tendência")

    st.line_chart(
        df_recentes.set_index("DATA")[estatistica]
    )