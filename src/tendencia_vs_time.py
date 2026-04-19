def tendencia_vs_time(df, adversario, estatistica, linha):

    df_time = df[df["ADVERSARIO"] == adversario.upper()]

    if df_time.empty:

        print("Nenhum jogo encontrado contra esse adversário.")

        return


    print(f"\n🏀 Jogos contra {adversario.upper()}:\n")


    for i, row in df_time.iterrows():

        print(
            f"{row['DATA']} → {row[estatistica]} {estatistica}"
        )


    acertos = (df_time[estatistica] >= linha).sum()

    total = len(df_time)

    porcentagem = (acertos / total) * 100


    print("\nResumo:")


    print(
        f"{acertos}/{total} jogos ({porcentagem:.1f}%) "
        f"com {linha}+ em {estatistica}"
    )