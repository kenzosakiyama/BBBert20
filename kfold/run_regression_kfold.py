from argparse import ArgumentParser
from typing import List, Tuple, Dict
from sklearn.model_selection import KFold, GridSearchCV
import pandas as pd 
import numpy as np 
import os

from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.linear_model import LinearRegression


PATH_TO_DATA = "../analysis/data/"
COLUMNS = ["paredao", "nome", 
           "positivos", "neutros","negativos", 
           "positivos_individual_pct", "neutros_individual_pct", "negativos_individual_pct",
           "positivos_global_pct", "neutros_global_pct", "negativos_global_pct",
           "day1", "day2", "day3",
           "likes", "retweets", "seguidores",
           "fica", "fora",
           "rejeicao"]

MODELS = {
    "linear_regression": LinearRegression()
}

METRICS = {
    "mse": mean_squared_error,
    "mae": mean_absolute_error
}

REMOVE = []

parser = ArgumentParser()

parser.add_argument("--model", required=True, type=str)
parser.add_argument("--folds", required=True, type=int)

parser.add_argument("--normalize", action="store_true")

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

def get_train_test(normalize: bool = True, drop_columns: List[str] = []) -> pd.DataFrame:

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

def evaluate(model, validation_data: Tuple[np.array, np.array]) -> Dict[str, List[float]]:
    _metrics = {metric: 0 for metric in METRICS.keys()}

    for metric in METRICS.keys():
        pred = model.predict(validation_data[0])
        val_target = validation_data[1]
        val_metric = METRICS[metric](val_target, pred)
        _metrics[metric] = val_metric

    return _metrics


def run_kfold(model, folds: int, normalize: bool) -> None:
    data_df = get_train_test(drop_columns=REMOVE, normalize=normalize)
    x, y = data_df.drop(columns=["paredao", "nome", "rejeicao"], axis=1).to_numpy(), data_df.drop(columns=data_df.columns[:-1], axis=1).to_numpy()
    _metrics = {metric: [] for metric in METRICS.keys()}

    skf = KFold(n_splits=folds, shuffle=True)

    for train_index, test_index in skf.split(x, y):
            X_train, X_test = x[train_index], x[test_index]
            y_train, y_test = y[train_index], y[test_index]

            model.fit(X_train, y_train)
            current_metrics = evaluate(model, (X_test, y_test))

            for metric in current_metrics.keys():
                _metrics[metric].append(current_metrics[metric])
    
    print(_metrics)


if __name__ == "__main__":
    args = parser.parse_args()

    model = MODELS[args.model]
    folds = args.folds
    normalize = args.normalize

    run_kfold(model, folds, normalize)