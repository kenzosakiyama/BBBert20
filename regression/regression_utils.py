import pandas as pd 
import numpy as np
import os 
from typing import Tuple, List

PATH_TO_DATA = "../analysis/data/"
COLUMNS = ["paredao", "nome", 
           "positivos", "neutros","negativos", 
           "positivos_individual_pct", "neutros_individual_pct", "negativos_individual_pct",
           "positivos_global_pct", "neutros_global_pct", "negativos_global_pct",
           "day1", "day2", "day3",
           "likes", "retweets", "seguidores",
           "fica", "fora",
           "rejeicao"]

def minmax_normalize(df: pd.DataFrame, classification: bool = False) -> pd.DataFrame:
    
    x, y = 0, 0
    
    for column in COLUMNS:
        if column == "paredao" or column == "nome" or "_pct" in column or (column == "rejeicao" and classification): continue
        # print(column)
        min_value = df[column].min()
        max_value = df[column].max()

        if column == "rejeicao": x, y = min_value, (max_value - min_value)

        df[column] = (df[column] - min_value) / (max_value - min_value)
    
    return df, x, y

def fix_types(df: pd.DataFrame) -> pd.DataFrame:

    for column in df.columns[2:]:
        if df[column].dtype == "O": df[column] = df[column].astype(int)

    return df

def get_train_test(test_paredao: int, normalize: bool = True, classification: bool = False, drop_columns: List[str] = [], data_path: str = PATH_TO_DATA) -> Tuple[pd.DataFrame, pd.DataFrame]:

    paredoes = os.listdir(data_path)
    data_df = pd.DataFrame(columns=COLUMNS)

    for paredao in paredoes:
        if not os.path.exists(os.path.join(data_path, paredao, "paredao_atributes.csv")): continue
        current = pd.read_csv(os.path.join(data_path, paredao, "paredao_atributes.csv"))

        if classification:
            index = current["rejeicao"].idxmax()
            classes = np.zeros(len(current))
            classes[index] = 1
            current["rejeicao"] = classes

        number = int(paredao.replace("paredao", ""))
        current["paredao"] = [number] * len(current)
        data_df = data_df.append(current, ignore_index=True, sort=False)

    data_df = fix_types(data_df)
    if normalize: data_df, mean, std = minmax_normalize(data_df, classification=classification)
    if len(drop_columns) > 0: data_df.drop(columns=drop_columns, inplace=True)

    test_df = data_df[data_df["paredao"] == test_paredao]
    train_df = data_df.drop(index=test_df.index, axis=0)

    return (train_df, test_df) if not normalize else (train_df, test_df, mean, std)