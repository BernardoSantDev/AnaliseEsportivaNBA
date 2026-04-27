import streamlit as st

def tendencia_recente(df, estatistica, linha, ultimos_jogos):

    df_recente = df.head(ultimos_jogos)

    acertos = (df_recente[estatistica] >= linha).sum()
    total = len(df_recente)
    porcentagem = (acertos / total) * 100

    st.write("Últimos jogos analisados")

    # tabela bonita
    tabela = df_recente[["DATA", "ADVERSARIO", estatistica]].copy()
    tabela["DATA"] = tabela["DATA"].dt.strftime("%d/%m/%Y")

    st.dataframe(tabela)

    st.success(
        f"{acertos}/{total} jogos ({porcentagem:.1f}%) "
        f"com {linha}+ em {estatistica} "
        f"nos últimos {ultimos_jogos} jogos"
    )