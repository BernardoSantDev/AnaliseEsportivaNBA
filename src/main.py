from data_loader import carregar_dados_jogador
from cleaning import limpar_dados
from tendencia_recente import tendencia_recente
from tendencia_vs_time import tendencia_vs_time
from tendencia_por_minutos import tendencia_por_minutos


def main():
    print("\n=== ANALISADOR DE PROPS NBA ===\n")

    jogador = input("Nome do jogador: ")

    estatistica = input(
        "Estatística (PONTOS / ASSISTENCIAS / REBOTES / C3_CONVERTIDOS / LL_CONVERTIDOS): "
    ).upper()

    linha = float(input("Linha da aposta: "))

    adversario = input("Adversário (ex: BOS, CHA, LAL): ").upper()

    ultimos_jogos = int(input("Últimos quantos jogos analisar? "))

    print("\nModo de análise:")
    print("1 - Regular Season")
    print("2 - Playoffs")
    print("3 - Ambos")
    tipo_temporada = input("Escolha: ")


    df = carregar_dados_jogador(jogador, tipo_temporada)


    if df is None:
        return


    df = limpar_dados(df)

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

    print("\n⏱️ Análise por minutos jogados:")
    usar_filtro = input("Deseja filtrar por minutos? (S/N): ").upper()
    if usar_filtro == "S":
        min_minutos = int(input("Minutos mínimos: "))
        max_minutos = int(input("Minutos máximos: "))
        tendencia_por_minutos(
            df,
            estatistica,
            linha,
            min_minutos,
            max_minutos
        )


if __name__ == "__main__":

    main()