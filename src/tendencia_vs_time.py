import streamlit as st

def tendencia_vs_time(df, estatistica, linha, adversario):

    df_time = df[df["ADVERSARIO"].str.upper() == adversario.upper()]
    if df_time.empty:
        st.warning("Nenhum jogo encontrado contra esse adversário.")
        return

    st.write(f"🏀 Jogos contra {adversario}")

    tabela = df_time[["DATA", estatistica]].copy()
    tabela["DATA"] = tabela["DATA"].dt.strftime("%d/%m/%Y")

    st.dataframe(tabela)

    acertos = (df_time[estatistica] >= linha).sum()
    total = len(df_time)
    porcentagem = (acertos / total) * 100

    st.success(
        f"{acertos}/{total} jogos ({porcentagem:.1f}%) "
        f"com {linha}+ em {estatistica}"
    )