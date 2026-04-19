def limpar_dataframe(df):

    df = df.rename(columns={
        "GAME_DATE": 'DATA',
        "PTS": 'PONTOS',
        "AST": 'ASSISTENCIA',
        "REB": 'REBOTES',
        "FG3M": "C3_CONVERTIDOS",
        "FG3A": "C3_TENTADOS",
        "FTM": "LL_CONVERTIDOS",
        "FTA": "LL_TENTADOS",
        "MIN": "MINUTOS"
    })

    #extraindo a sigla do adversario
    df['ADVERSARIO'] = df['MATCHUP'].str[-3:]

    #garantindo que os jogos mais recentes ficam no topo
    df = df.sort_values(by="DATA", ascending=False)

    df = df.reset_index(drop=True)

    return df