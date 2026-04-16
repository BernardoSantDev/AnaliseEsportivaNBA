from nba_api.stats.static import players
from nba_api.stats.endpoints import playergamelog

def buscar_player_id(nome_jogador):
    lista_players = players.get_players()
    for player in lista_players:
        if player['full_name'].lower() == nome_jogador.lower():
            return player['id']
    return None