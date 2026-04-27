import streamlit as st

def calcular_medias(df, estatistica, adversario, ultimos):

    df_recentes = df.head(ultimos)
    media_recentes = df_recentes[estatistica].mean()

    df_vs_time = df[df["ADVERSARIO"] == adversario]

    media_temporada = df[estatistica].mean()

    st.write("📈 Médias comparativas")

    st.metric("Últimos jogos", f"{media_recentes:.1f}")
    st.metric("Temporada", f"{media_temporada:.1f}")

    if len(df_vs_time) > 0:
        media_vs_time = df_vs_time[estatistica].mean()
        st.metric(f"Vs {adversario}", f"{media_vs_time:.1f}")
    else:
        st.warning(f"Sem jogos contra {adversario}")