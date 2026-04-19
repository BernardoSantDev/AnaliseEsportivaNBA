def tendencia_recente(df, estatistica, linha, ultimos_jogos):

    df_recente = df.head(ultimos_jogos)

    acertos = (df_recente[estatistica] >= linha).sum()

    total = len(df_recente)

    porcentagem = (acertos / total) * 100


    print("\n📊 Últimos jogos analisados:\n")


    for i, row in df_recente.iterrows():

        print(
            f"{row['DATA'].strftime('%d/%m/%Y')} | vs {row['ADVERSARIO']} → "
            f"{row[estatistica]} {estatistica}"
        )


    print("\nResumo:")


    print(
        f"{acertos}/{total} jogos ({porcentagem:.1f}%) "
        f"com {linha}+ em {estatistica} "
        f"nos últimos {ultimos_jogos} jogos"
    )