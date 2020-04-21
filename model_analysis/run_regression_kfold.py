from argparse import ArgumentParser
from typing import List, Tuple, Dict
from sklearn.model_selection import KFold, GridSearchCV
import pandas as pd 
import numpy as np 
import os

from model_utils import *
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import AdaBoostRegressor, RandomForestRegressor
from sklearn.svm import SVR


MODELS = {
    "linear_regression": LinearRegression(),
    "svm": SVR(C=0.7, kernel="linear"),
    "ada_boost": AdaBoostRegressor(n_estimators=100, learning_rate=1, loss="linear"),
    "random_forest": RandomForestRegressor(n_estimators=100),
    "knn": KNeighborsRegressor(n_neighbors=5, metric="minkowski")
}


def build_parser() -> ArgumentParser:
    parser = ArgumentParser()

    parser.add_argument("--model", required=True, type=str)
    parser.add_argument("--folds", required=True, type=int)

    parser.add_argument("--normalize", action="store_true")

    return parser


def run_kfold(model, folds: int, normalize: bool) -> None:
    data_df = get_data(drop_columns=REMOVE, normalize=normalize)
    x, y = data_df.drop(columns=["paredao", "nome", "rejeicao"], axis=1).to_numpy(), data_df.drop(columns=data_df.columns[:-1], axis=1).to_numpy()
    y = np.ravel(y)
    _metrics = {metric: [] for metric in METRICS.keys()}

    skf = KFold(n_splits=folds, shuffle=True)

    for train_index, test_index in skf.split(x, y):
            X_train, X_test = x[train_index], x[test_index]
            y_train, y_test = y[train_index], y[test_index]

            model.fit(X_train, y_train)
            current_metrics = evaluate(model, (X_test, y_test))

            for metric in current_metrics.keys():
                _metrics[metric].append(current_metrics[metric])
    
    # Averaging metrics
    for metric in _metrics:
        _metrics[metric] = (np.mean(_metrics[metric]), np.std(_metrics[metric]))

    print(_metrics)


if __name__ == "__main__":
    parser = build_parser()
    args = parser.parse_args()

    model = MODELS[args.model]
    folds = args.folds
    normalize = args.normalize

    run_kfold(model, folds, normalize)