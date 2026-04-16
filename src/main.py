from data_loader import carregar_dados
from tendencia_recente import tendencia_recente
from tendencia_vs_time import tendencia_vs_time

def main():
    df = carregar_dados()

    print("----ANALISADOR DE PROPS NBA----")
    coluna = input("Estatística você quer analisar? (ex: PONTOS, REBOTES): ")
    limite = float(input("Limite da aposta (ex: 25): "))
    adversario = input("Adversário do jogador (ex: BOS): ")
    Ultimos_jogos = int(input("Número de jogos recentes para análise (ex: 5): "))
