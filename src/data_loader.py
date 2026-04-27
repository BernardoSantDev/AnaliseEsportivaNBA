from nba_api.stats.static import players
from nba_api.stats.endpoints import playergamelog
from datetime import datetime
import unicodedata
import pandas as pd
import streamlit as st


#Criando uma função para checar qual a temporada atual
def temporada_atual():
    hoje = datetime.now()
    ano = hoje.year
    mes = hoje.month

    if mes >= 10:  # Se for outubro ou depois, a temporada é do ano atual
        return f"{ano}-{str(ano+1)[-2:]}"
    else:
        return f"{ano-1}-{str(ano)[-2:]}"



#Essa função eu utilizo para buscar o ID do jogador a partir do nome completo, pois a API da NBA utiliza o ID para realizar as consultas de dados. 
#A função percorre a lista de jogadores disponíveis e compara o nome completo com o nome fornecido, retornando o ID correspondente. 
# Se o jogador não for encontrado, a função retorna None.

def remover_acentos(texto):

    return unicodedata.normalize(
        "NFKD", texto
    ).encode(
        "ASCII", "ignore"
    ).decode("ASCII")


def buscar_player_id(nome_jogador):

    nome_input = remover_acentos(nome_jogador.lower())

    lista_players = players.get_players()

    for player in lista_players:

        nome_api = remover_acentos(
            player["full_name"].lower()
        )

        if nome_input in nome_api:

            return player["id"]

    print(f"Jogador '{nome_jogador}' não encontrado.")

    return None


@st.cache_data(ttl=3600)
def carregar_dados_jogador(nome_jogador, tipo_temporada):

    player_id = buscar_player_id(nome_jogador)

    if player_id is None:
        return None

    season = temporada_atual()

    arquivo_cache = f"data/cache/cache_{player_id}.csv"
    def fetch(tipo):
        return playergamelog.PlayerGameLog(
            player_id=player_id,
            season=season,
            season_type_all_star=tipo,
            timeout=60
        ).get_data_frames()[0]

    # 🔁 TENTAR BUSCAR DA API (3 vezes)
    import time
    for tentativa in range(3):
        try:

            if tipo_temporada == "1":
                df = fetch("Regular Season")

            elif tipo_temporada == "2":
                df = fetch("Playoffs")

            elif tipo_temporada == "3":
                regular = fetch("Regular Season")
                playoffs = fetch("Playoffs")
                df = pd.concat([regular, playoffs])

            else:
                return None

            # 💾 SALVA CSV
            df.to_csv(arquivo_cache, index=False)

            return df

        except Exception:
            time.sleep(2)

    # 💥 FALLBACK → CSV
    try:
        df = pd.read_csv(arquivo_cache)
        return df
    except:
        return None
