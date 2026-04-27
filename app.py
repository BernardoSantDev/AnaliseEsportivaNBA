import streamlit as st
from src.data_loader import carregar_dados_jogador
from src.cleaning import limpar_dados
from src.tendencia_recente import tendencia_recente
from src.tendencia_vs_time import tendencia_vs_time
from src.tendencia_por_minutos import tendencia_por_minutos
from src.medias_estatisticas import calcular_medias

st.set_page_config(page_title="NBA Props Analizador", layout="centered")

st.title("Analizador de Estatistica da NBA")
st.write("Analise tendências estatísticas de jogadores da NBA")

nome = st.text_input("Nome do jogador")

estatistica = st.selectbox( "Estatística", [ 
    "PONTOS", 
    "ASSISTENCIAS", 
    "REBOTES", 
    "REBOTES_OFENSIVOS", 
    "REBOTES_DEFENSIVOS", 
    "ROUBOS", 
    "TOCOS", 
    "TURNOVERS", 
    "C3_CONVERTIDOS", 
    "C3_TENTADOS", 
    "LL_CONVERTIDOS", 
    "LL_TENTADOS", 
    "MINUTOS", 
    "PLUS_MINUS" 
    ])

linha = st.number_input("Linha da aposta", value=10)
adversario = st.text_input("Adversário (ex: BOS, LAL, MIN)")

tipo_temporada = st.selectbox( 
    "Tipo de temporada", 
    [ 
        "Regular Season",
        "Playoffs", 
        "Ambos" 
    ] )

mapa_temporada = {
    "Regular Season": "1",
    "Playoffs": "2",
    "Ambos": "3"
}

ultimos = st.slider("Últimos jogos analisados", 5, 20, 10)
usar_minutos = st.checkbox("Filtrar por minutos jogados")

if usar_minutos:
    min_min = st.number_input("Min minutos", value=20)
    max_min = st.number_input("Max minutos", value=40)


if st.button("Analisar jogador"):
    if nome == "" or adversario == "":
        st.warning("Preencha jogador e adversário")
    else:
        df = carregar_dados_jogador(
            nome,
            mapa_temporada[tipo_temporada]
        )
        if df is None:
            st.error("Jogador não encontrado")
        else:
            df = limpar_dados(df)
            st.subheader("📊 Tendência recente")
            tendencia_recente(
                df,
                estatistica,
                linha,
                ultimos
            )
            st.subheader("🏀 Tendência vs adversário")
            tendencia_vs_time(
                df,
                estatistica,
                linha,
                adversario.upper()
            )
            if usar_minutos:
                st.subheader("⏱️ Tendência por minutos")
                tendencia_por_minutos(
                    df,
                    estatistica,
                    linha,
                    min_min,
                    max_min
                )
            st.subheader("📈 Médias comparativas")
            calcular_medias(
                df,
                estatistica,
                adversario.upper(),
                ultimos
            )