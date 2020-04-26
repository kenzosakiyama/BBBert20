from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.linear_model import LinearRegression, Lasso, ElasticNet, Ridge
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import AdaBoostRegressor, RandomForestRegressor, VotingRegressor
from sklearn.svm import SVR
from typing import List, Dict, Tuple
import pandas as pd
import os
import numpy as np

PATH_TO_DATA = "../analysis/data/"

REMOVE = ["positivos", "neutros", "negativos", "likes", "retweets", "day2", "day3"]

COLUMNS = ["paredao", "nome", 
           "positivos", "neutros","negativos", 
           "positivos_individual_pct", "neutros_individual_pct", "negativos_individual_pct",
           "positivos_global_pct", "neutros_global_pct", "negativos_global_pct",
           "day1", "day2", "day3",
           "likes", "retweets", "seguidores",
           "fica", "fora",
           "rejeicao"]

MODELS = {
    "linear_regression": LinearRegression,
    "svm": SVR,
    "ada_boost": AdaBoostRegressor,
    "random_forest": RandomForestRegressor,
    "knn": KNeighborsRegressor,
    "lasso": Lasso,
    "ridge": Ridge,
    "elastic_net": ElasticNet,
    "ensamble1": VotingRegressor
}

PARAMETERS = {
    "linear_regression": {"normalize": False},
    "svm": {"C": 0.95, "epsilon": 0.35, "kernel": "rbf"},
    "ada_boost": {"n_estimators": 100, "learning_rate": 0.85, "loss": "exponential"},
    "random_forest": {"n_estimators": 1000},
    "knn": {"n_neighbors": 3, "metric": "minkowski", "p": 1},
    "lasso": {"alpha": 0.1},
    "ridge": {"alpha": 10},
    "elastic_net": {"alpha": 0.4, "l1_ratio": 0}
}

PARAMETERS["ensamble1"] = {"estimators": [("svm", SVR(**PARAMETERS["svm"])), ("lr", LinearRegression()), ("elastic", ElasticNet(**PARAMETERS["elastic_net"]))]}

NORMALIZE = {
    "linear_regression": True,
    "svm": True,
    "ada_boost": False,
    "random_forest": False,
    "knn": True,
    "lasso": True,
    "ridge": True,
    "elastic_net": True,
    "ensamble1": True
}

METRICS = {
    "mse": mean_squared_error,
    "mae": mean_absolute_error,
    "r2": r2_score
}

def zscore_normalize(df: pd.DataFrame) -> pd.DataFrame:
    
    y_mean, y_std = 0, 0
    
    for column in COLUMNS:
        if column == "paredao" or column == "nome": continue
        mean = df[column].mean()
        std = df[column].std()

        if column == "rejeicao": y_mean, y_std = mean, std

        df[column] = (df[column] - mean) / std
    
    return df, y_mean, y_std

def fix_types(df: pd.DataFrame) -> pd.DataFrame:

    for column in df.columns[2:]:
        if df[column].dtype == "O": df[column] = df[column].astype(int)

    return df

def get_data(normalize: bool = True, drop_columns: List[str] = []) -> pd.DataFrame:

    paredoes = os.listdir(PATH_TO_DATA)
    data_df = pd.DataFrame(columns=COLUMNS)

    for paredao in paredoes:
        if not os.path.exists(os.path.join(PATH_TO_DATA, paredao, "paredao_atributes.csv")): continue
        current = pd.read_csv(os.path.join(PATH_TO_DATA, paredao, "paredao_atributes.csv"))

        number = int(paredao.replace("paredao", ""))
        current["paredao"] = [number] * len(current)
        data_df = data_df.append(current, ignore_index=True, sort=False)

    data_df = fix_types(data_df)
    if normalize: data_df, mean, std = zscore_normalize(data_df)
    if len(drop_columns) > 0: data_df.drop(columns=drop_columns, inplace=True)

    return data_df

def evaluate(model, validation_data: Tuple[np.array, np.array]) -> Dict[str, float]:
    _metrics = {metric: 0 for metric in METRICS.keys()}

    for metric in METRICS.keys():
        pred = model.predict(validation_data[0])
        val_target = validation_data[1]
        val_metric = METRICS[metric](val_target, pred)
        _metrics[metric] = val_metric

    return _metrics