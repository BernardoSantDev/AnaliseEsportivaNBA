import pandas as pd


def limpar_dados(df):

    df = df.rename(columns={

        "GAME_DATE": "DATA",
        "MATCHUP": "CONFRONTO",
        "WL": "RESULTADO",
        "MIN": "MINUTOS",
        "FGM": "CESTAS_CONVERTIDAS",
        "FGA": "CESTAS_TENTADAS",
        "FG3M": "C3_CONVERTIDOS",
        "FG3A": "C3_TENTADOS",
        "FTM": "LL_CONVERTIDOS",
        "FTA": "LL_TENTADOS",
        "REB": "REBOTES",
        "AST": "ASSISTENCIAS",
        "STL": "ROUBOS",
        "BLK": "TOCOS",
        "PTS": "PONTOS"

    })


    df["ADVERSARIO"] = df["CONFRONTO"].str[-3:]


    df["FG_%"] = df["CESTAS_CONVERTIDAS"] / df["CESTAS_TENTADAS"].replace(0, None)
    df["C3_%"] = df["C3_CONVERTIDOS"] / df["C3_TENTADOS"].replace(0, None)
    df["LL_%"] = df["LL_CONVERTIDOS"] / df["LL_TENTADOS"].replace(0, None)


    df["DATA"] = pd.to_datetime(df["DATA"])

    df = df.sort_values("DATA", ascending=False)

    df = df.reset_index(drop=True)


    return df