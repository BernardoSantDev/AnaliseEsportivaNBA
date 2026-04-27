import streamlit as st

def calcular_probabilidade(df, estatistica, linha, ultimos):

    df_recentes = df.head(ultimos)

    acertos = (df_recentes[estatistica] >= linha).sum()
    total = len(df_recentes)

    prob = acertos / total
    porcentagem = prob * 100

    # evitar divisão por zero
    if prob == 0:
        odd_justa = 0
    else:
        odd_justa = 1 / prob

    st.write("🎯 Probabilidade")

    col1, col2 = st.columns(2)

    col1.metric("Probabilidade", f"{porcentagem:.1f}%")
    col2.metric("Odd justa", f"{odd_justa:.2f}" if odd_justa != 0 else "-")

    # insight automático
    if prob >= 0.7:
        st.success("🔥 Alta probabilidade (linha interessante)")
    elif prob >= 0.5:
        st.warning("⚠️ Probabilidade moderada")
    else:
        st.error("❌ Baixa probabilidade")