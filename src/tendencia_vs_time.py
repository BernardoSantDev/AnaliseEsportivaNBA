def tendencia_vs_time(df, adversario, estatistica, linha):
    df_time = df[df["ADVERSARIO"] == adversario.upper()]

    if df_time.empty:

        print("Nenhum jogo encontrado contra esse adversário.")

        return

    acertos = (df_time[estatistica] >= linha).sum()

    total = len(df_time)

    porcentagem = (acertos / total) * 100

    print(
        f"Contra {adversario.upper()}: "
        f"{acertos}/{total} jogos ({porcentagem:.1f}%) "
        f"com {linha}+ em {estatistica}"
    )

















