from data_loader import carregar_dados_jogador
from cleaning import limpar_dataframe
from tendencia_recente import tendencia_recente
from tendencia_vs_time import tendencia_vs_time


def main():
    print("\n=== ANALISADOR DE PROPS NBA ===\n")

    jogador = input("Nome do jogador: ")

    estatistica = input(
        "Estatística (PONTOS / ASSISTENCIAS / REBOTES / C3_CONVERTIDOS / LL_CONVERTIDOS): "
    ).upper()

    linha = float(input("Linha da aposta: "))

    adversario = input("Adversário (ex: BOS, CHA, LAL): ").upper()

    ultimos_jogos = int(input("Últimos quantos jogos analisar? "))


    df = carregar_dados_jogador(jogador)

    if df is None:

        return


    df = limpar_dataframe(df)


    print("\n📊 Tendência recente:\n")

    tendencia_recente(
        df,
        estatistica,
        linha,
        ultimos_jogos
    )


    print("\n🏀 Tendência vs adversário:\n")

    tendencia_vs_time(
        df,
        adversario,
        estatistica,
        linha
    )


if __name__ == "__main__":

    main()