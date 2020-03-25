import pandas as pd 
import numpy as np
import os 
from typing import Tuple

PATH_TO_DATA = "../analysis/data/"
COLUMNS = ["paredao", "nome", "positivos", "neutros","negativos", "positivos_pct", "neutros_pct", "negativos_pct", "seguidores", "rejeicao"]

def zscore_normalize(df: pd.DataFrame, classification: bool = False) -> pd.DataFrame:
    
    y_mean, y_std = 0, 0
    
    for column in COLUMNS:
        if column == "paredao" or column == "nome" or (column == "rejeicao" and classification) : continue
        mean = df[column].mean()
        std = df[column].std()

        if column == "rejeicao": y_mean, y_std = mean, std

        df[column] = (df[column] - mean) / std
    
    return df, y_mean, y_std

def get_train_test(test_paredao: int, normalize: bool = True, classification: bool = False) -> Tuple[pd.DataFrame, pd.DataFrame]:

    paredoes = os.listdir(PATH_TO_DATA)
    data_df = pd.DataFrame(columns=COLUMNS)

    for paredao in paredoes:
        current = pd.read_csv(os.path.join(PATH_TO_DATA, paredao, "paredao_atributes.csv"))

        if classification:
            index = current["rejeicao"].idxmax()
            classes = np.zeros(len(current))
            classes[index] = 1
            current["rejeicao"] = classes

        number = int(paredao.replace("paredao", ""))
        current["paredao"] = [number] * len(current)
        data_df = data_df.append(current, ignore_index=True, sort=False)

    if normalize: data_df, mean, std = zscore_normalize(data_df, classification=classification)

    test_df = data_df[data_df["paredao"] == test_paredao]
    train_df = data_df.drop(index=test_df.index, axis=0)

    return (train_df, test_df) if not normalize else (train_df, test_df, mean, std)