from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.linear_model import LinearRegression, Lasso, ElasticNet, Ridge, SGDRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import AdaBoostRegressor, RandomForestRegressor, VotingRegressor, BaggingRegressor
from sklearn.svm import SVR
from typing import List, Dict, Tuple
import pandas as pd
import os
import numpy as np

PATH_TO_DATA = "../analysis/data/"

# Remove all sentiment analysis infos
# REMOVE = ["positivos_individual_pct", "neutros_individual_pct", "negativos_individual_pct","positivos_global_pct", "neutros_global_pct", "negativos_global_pct","positivos", "neutros", "negativos", "likes", "retweets", "day2", "day3"]

KEEP = [
    "positivos",
    "neutros_individual_pct",
    "negativos_individual_pct",
    "positivos_global_pct",
    "negativos_global_pct",
    "seguidores",
    "fora"
]

REMOVE = [
    'positivos_global_pct',
    'neutros_global_pct', 
    'neutros', 'negativos',
    'day3', 'day2', 'day1', 
    'fica', 'likes', 'retweets'
]

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
    "svr": SVR,
    "ada_boost": AdaBoostRegressor,
    "random_forest": RandomForestRegressor,
    "knn": KNeighborsRegressor,
    "lasso": Lasso,
    "ridge": Ridge,
    "elastic_net": ElasticNet,
    "sgd": SGDRegressor,
    "ensamble3": VotingRegressor,
    "ensamble2": BaggingRegressor
}

PARAMETERS = {
    "linear_regression": {"normalize": False},
    "svr": {'C': 0.95, 'degree': 5, 'epsilon': 0.05, 'kernel': 'rbf'},
    "ada_boost": {'learning_rate': 0.85, 'loss': 'linear', 'n_estimators': 100},
    "random_forest": {"n_estimators": 1000, 'criterion': 'mae'},
    "knn": {"n_neighbors": 5, "metric": "minkowski", "p": 1},
    "lasso": {"alpha": 0.01},
    "ridge": {"alpha": 0.5},
    "elastic_net": {"alpha": 0.1, "l1_ratio": 0.0},
    "sgd":{'alpha': 0.01, 'epsilon': 0.2, 'l1_ratio': 0.2, 'learning_rate': 'optimal', 'loss': 'epsilon_insensitive', 'penalty': 'elasticnet'}
}

PARAMETERS["ensamble3"] = {
    "estimators": [
        ("svr", SVR(**PARAMETERS["svr"])), 
        ("knn", KNeighborsRegressor(**PARAMETERS["knn"])),
        ("ridge", Ridge(**PARAMETERS["ridge"]))
    ]
}

PARAMETERS["ensamble2"] = {
    "base_estimator": SVR(**PARAMETERS["svr"]),
    "n_estimators": 5
}

NORMALIZE = {
    "linear_regression": True,
    "svr": True,
    "ada_boost": False,
    "random_forest": False,
    "knn": True,
    "lasso": True,
    "ridge": True,
    "elastic_net": True,
    "sgd": True,
    "ensamble3": True,
    "ensamble2": True
}

METRICS = {
    "mse": mean_squared_error,
    "mae": mean_absolute_error,
    "r2": r2_score
}

def minmax_normalize(df: pd.DataFrame) -> pd.DataFrame:
    
    x, y = 0, 0
    
    for column in COLUMNS:
        if column == "paredao" or column == "nome" or "_pct" in column: continue
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
    if normalize: data_df, _, _ = minmax_normalize(data_df)
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