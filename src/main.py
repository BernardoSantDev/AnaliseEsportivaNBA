from data_loader import carregar_dados
from tendencia_recente import tendencia_recente
from tendencia_vs_time import tendencia_vs_time

def main():
    df = carregar_dados()

    print("----ANALISADOR DE PROPS NBA----")
    coluna = input("Estatística você quer analisar? (ex: PONTOS, REBOTES): ")
    limite = float(input("Limite da aposta (ex: 25): "))
    adversario = input("Adversário do jogador (ex: BOS): ")
    ultimos_jogos = int(input("Número de jogos recentes para análise (ex: 5): "))

    print("\nRESULTADOS DA ANÁLISE:\n")
    tendencia_recente(df, coluna, limite, ultimos_jogos)
    tendencia_vs_time(df, adversario, coluna, limite)

if __name__ == "__main__":
    main()