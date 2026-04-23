from nba_api.stats.static import players
from nba_api.stats.endpoints import playergamelog
from datetime import datetime
import unicodedata
import pandas as pd


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


#Cria a função para carregar os dados do jogador, utilizando o ID obtido pela função anterior.
def carregar_dados_jogador(nome_jogador):
    season = temporada_atual()
    player_id = buscar_player_id(nome_jogador)

    if player_id is None:
        print(f"Jogador '{nome_jogador}' não encontrado.")
        return None
    


    # temporada regular
    gamelog_regular  = playergamelog.PlayerGameLog(
        player_id=player_id, 
        season=season,
        season_type_all_star="Regular Season"
    )
    
    df_regular = gamelog_regular.get_data_frames()[0]


    # playoffs
    gamelog_playoffs = playergamelog.PlayerGameLog(
        player_id=player_id,
        season=season,
        season_type_all_star="Playoffs"
    )

    df_playoffs = gamelog_playoffs.get_data_frames()[0]

    # juntar datasets
    df_total = pd.concat(
        [df_regular, df_playoffs],
        ignore_index=True
    )

    # ordenar do mais recente para o mais antigo
    df_total["GAME_DATE"] = pd.to_datetime(
        df_total["GAME_DATE"]
    )

    df_total = df_total.sort_values(
        by="GAME_DATE",
        ascending=False
    )
    print(f"Temporada carregada automaticamente: {season}")
    print("Incluindo temporada regular + playoffs")


    return df_total
