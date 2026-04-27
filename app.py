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