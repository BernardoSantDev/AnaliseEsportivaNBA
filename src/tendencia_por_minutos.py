def tendencia_por_minutos(df, estatistica, linha, min_minutos, max_minutos):
    
    df_filtrado = df[
        (df["MINUTOS"] >= min_minutos) &
        (df["MINUTOS"] <= max_minutos)
    ]

    total = len(df_filtrado)

    if total == 0:
        print("\nNenhum jogo encontrado nesse intervalo de minutos.")
        return
    
    acertos = len(df_filtrado[df_filtrado[estatistica] >= linha])

    percentual = (acertos / total) * 100

    print(
        f"\n{acertos}/{total} jogos ({percentual:.1f}%) com "
        f"{linha}+ em {estatistica} entre {min_minutos}-{max_minutos} minutos"
    )

    print("\nJogos analisados:\n")

    for _, row in df_filtrado.iterrows():

        print(
            f"{row['DATA'].strftime('%d/%m/%Y')} | "
            f"vs {row['ADVERSARIO']} → "
            f"{row[estatistica]} {estatistica} "
            f"({row['MINUTOS']} min)"
        )