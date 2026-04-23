def calcular_medias(df, estatistica, adversario, ultimos):

    print("\n📊 Médias comparativas:\n")

    # Média últimos jogos
    df_recentes = df.head(ultimos)
    media_recentes = df_recentes[estatistica].mean()
    print(
        f"Média últimos {ultimos} jogos → {media_recentes:.1f}"
    )


    # Média vs adversário
    df_vs_time = df[df["ADVERSARIO"] == adversario]
    if len(df_vs_time) > 0:
        media_vs_time = df_vs_time[estatistica].mean()
        print(
            f"Média vs {adversario} → {media_vs_time:.1f}"
        )
    else:
        print(f"Sem jogos contra {adversario}")


    # Média temporada
    media_temporada = df[estatistica].mean()
    print(
        f"Média temporada → {media_temporada:.1f}"
    )