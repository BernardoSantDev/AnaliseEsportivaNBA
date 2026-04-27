import streamlit as st

def tendencia_por_minutos(df, estatistica, linha, min_minutos, max_minutos):
    
    df_filtrado = df[
        (df["MINUTOS"] >= min_minutos) &
        (df["MINUTOS"] <= max_minutos)
    ]

    total = len(df_filtrado)

    if total == 0:
        st.warning("Nenhum jogo encontrado nesse intervalo de minutos.")
        return
    
    acertos = (df_filtrado[estatistica] >= linha).sum()
    percentual = (acertos / total) * 100

    st.write("⏱️ Jogos analisados")

    tabela = df_filtrado[["DATA", "ADVERSARIO", estatistica, "MINUTOS"]].copy()
    tabela["DATA"] = tabela["DATA"].dt.strftime("%d/%m/%Y")

    st.dataframe(tabela)

    st.success(
        f"{acertos}/{total} jogos ({percentual:.1f}%) com "
        f"{linha}+ em {estatistica} entre {min_minutos}-{max_minutos} minutos"
    )