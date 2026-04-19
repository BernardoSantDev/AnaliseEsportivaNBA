def tendencia_recente(df, estatistica, linha, ultimos_jogos):
    df_recente  = df.head(ultimos_jogos)

    acertos = (df_recente[estatistica] >= linha).sum()

    total = len(df_recente)

    porcentagem = (acertos / total) * 100

    print(
        f"{acertos}/{total} jogos ({porcentagem:.1f}%) "
        f"com {linha}+ em {estatistica} nos últimos {ultimos_jogos} jogos"
    )