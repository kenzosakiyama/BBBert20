from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.linear_model import LinearRegression, Lasso, ElasticNet, Ridge, SGDRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import AdaBoostRegressor, RandomForestRegressor, VotingRegressor, BaggingRegressor
from sklearn.svm import SVR
from sklearn.feature_selection import RFE
from sklearn.model_selection import cross_val_predict
from typing import List, Dict, Tuple
import pandas as pd
import os
import numpy as np


PATH_TO_DATA = "../analysis/data/"

# Remove all sentiment analysis infos
# REMOVE = ["positivos_individual_pct", "neutros_individual_pct", "negativos_individual_pct","positivos_global_pct", "neutros_global_pct", "negativos_global_pct","positivos", "neutros", "negativos", "likes", "retweets", "day2", "day3"]

COLUMNS = [
    "positivos", "neutros","negativos", 
    "positivos_individual_pct", "neutros_individual_pct", "negativos_individual_pct",
    "positivos_global_pct", "neutros_global_pct", "negativos_global_pct",
    "day1", "day2", "day3",
    "likes", "retweets", "seguidores",
    "fica", "fora",
]

DEFAULT_COLUMNS = ["paredao", "nome", "rejeicao"]

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

PARAMETERS_ALL_ATRIBUTES = {
    "linear_regression": {"normalize": False},
    "svr": {'C': 0.95, 'degree': 4, 'epsilon': 0.1, 'kernel': 'rbf'},
    "ada_boost": {'learning_rate': 0.15, 'loss': 'square', 'n_estimators': 100},
    "random_forest": {"n_estimators": 100},
    "knn": {"n_neighbors": 3, "metric": "minkowski", "p": 2},
    "lasso": {"alpha": 0.01},
    "ridge": {"alpha": 0.5},
    "elastic_net": {"alpha": 0.1, "l1_ratio": 0.0},
    "sgd": {'alpha': 0.01, 'epsilon': 0.15, 'l1_ratio': 0.65, 'learning_rate': 'optimal', 'loss': 'epsilon_insensitive', 'penalty': 'l2'}
}

PARAMETERS = {
    "linear_regression": {"normalize": False},
    "svr": {'C': 0.95, 'degree': 4, 'epsilon': 0.1, 'kernel': 'rbf'},
    "ada_boost": {'learning_rate': 0.85, 'loss': 'linear', 'n_estimators': 100},
    "random_forest": {"n_estimators": 500},
    "knn": {"n_neighbors": 3, "metric": "minkowski", "p": 2},
    "lasso": {"alpha": 0.01},
    "ridge": {"alpha": 0.5},
    "elastic_net": {"alpha": 0.1, "l1_ratio": 0.0},
    "sgd": {'alpha': 0.001, 'epsilon': 0.15, 'l1_ratio': 0.7, 'learning_rate': 'constant', 'loss': 'epsilon_insensitive', 'penalty': 'l1'}
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
    
    for column in COLUMNS + DEFAULT_COLUMNS:
        if column == "paredao" or column == "nome" or "_pct" in column: continue
        # print(column)
        min_value = df[column].min()
        max_value = df[column].max()

        if column == "rejeicao": x, y = min_value, (max_value - min_value)

        df[column] = (df[column] - min_value) / (max_value - min_value)
    
    return df, x, y

def fix_types(df: pd.DataFrame) -> pd.DataFrame:

    for column in df.columns:
        if column in DEFAULT_COLUMNS: continue
        if df[column].dtype == "O": df[column] = df[column].astype(int)

    return df

def get_train_test(test_paredao: int, features: List[str], normalize: bool = True, data_path: str = PATH_TO_DATA) -> Tuple[pd.DataFrame, pd.DataFrame]:

    paredoes = os.listdir(data_path)
    data_df = pd.DataFrame(columns=COLUMNS+DEFAULT_COLUMNS)

    for paredao in paredoes:
        if not os.path.exists(os.path.join(data_path, paredao, "paredao_atributes.csv")): continue
        current = pd.read_csv(os.path.join(data_path, paredao, "paredao_atributes.csv"))

        number = int(paredao.replace("paredao", ""))
        current["paredao"] = [number] * len(current)
        data_df = data_df.append(current, ignore_index=True, sort=False)

    data_df = fix_types(data_df)

    if normalize: data_df, mean, std = minmax_normalize(data_df)

    # Feature selection
    data_df = data_df[features + DEFAULT_COLUMNS]

    test_df = data_df[data_df["paredao"] == test_paredao]
    train_df = data_df.drop(index=test_df.index, axis=0)

    return (train_df, test_df) if not normalize else (train_df, test_df, mean, std)

def get_data(features: List[str], normalize: bool = True) -> pd.DataFrame:

    paredoes = os.listdir(PATH_TO_DATA)
    data_df = pd.DataFrame(columns=COLUMNS+DEFAULT_COLUMNS)

    for paredao in paredoes:
        if not os.path.exists(os.path.join(PATH_TO_DATA, paredao, "paredao_atributes.csv")): continue
        current = pd.read_csv(os.path.join(PATH_TO_DATA, paredao, "paredao_atributes.csv"))

        number = int(paredao.replace("paredao", ""))
        current["paredao"] = [number] * len(current)
        data_df = data_df.append(current, ignore_index=True, sort=False)

    data_df = fix_types(data_df)
    if normalize: data_df, _, _ = minmax_normalize(data_df)
    data_df = data_df[features + DEFAULT_COLUMNS]

    return data_df

def evaluate(model, validation_data: Tuple[np.array, np.array]) -> Dict[str, float]:
    _metrics = {metric: 0 for metric in METRICS.keys()}

    for metric in METRICS.keys():
        pred = model.predict(validation_data[0])
        val_target = validation_data[1]
        val_metric = METRICS[metric](val_target, pred)
        _metrics[metric] = val_metric

    return _metrics

def get_minimum_features(regressor_model, x: np.array, y: np.array) -> int:
  
    best_score = 0
    n_features = 0           

    for n in range(1, len(COLUMNS)):
        rfe = RFE(regressor_model, n)
        X_train_rfe = rfe.fit_transform(x, y)
        preds = cross_val_predict(regressor_model, X_train_rfe, y, cv=10, n_jobs=5)
        score = r2_score(y, preds)

        if(score > best_score):
            best_score = score
            n_features = n

    return n_features

if __name__ == "__main__":
    pass