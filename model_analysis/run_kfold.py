from argparse import ArgumentParser
from typing import List, Tuple, Dict
from sklearn.model_selection import KFold, GridSearchCV
from run_grid_search import load_json
import pandas as pd 
import numpy as np 
import os
import json

from model_utils import *
from run_grid_search import load_json
from datetime import datetime
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.feature_selection import RFE
from sklearn.pipeline import Pipeline

def build_parser() -> ArgumentParser:

    parser = ArgumentParser()
    parser.add_argument("--model", required=True, type=str)
    parser.add_argument("--folds", type=int, default=10)

    return parser

def write_results(results: Dict[str, List[float]]) -> None:

    current_results = []
    if os.path.exists("kfold_results.json"):
        with open("kfold_results.json", "r") as f:
            current_results = json.load(f)
    
    current_results.append(results)

    with open("kfold_results.json", "w") as fout:
        json.dump(current_results, fout, indent=2)

def run_kfold(model_name: str, features: List[str], folds: int) -> None:

    params = PARAMETERS[model_name]
    regressor_model = MODELS[model_name]
    norm = NORMALIZE[model_name]
    # feat = features[model_name]
    # To use ALL features
    # norm = False

    data_df = get_data(features, normalize=norm)
    print(data_df[["paredao", "nome", "rejeicao"]].head(10))
    # Feature selection:
    print(f"- Model {model_name}")
    print(f"-- Features: {data_df.columns.to_list()}")
    print(f"-- Parameters: {params}")
    

    x, y = data_df.drop(columns=["paredao", "nome", "rejeicao"], axis=1).to_numpy(), data_df["rejeicao"].to_numpy()
    y = np.ravel(y)
    _metrics = {metric: [] for metric in METRICS.keys()}

    skf = KFold(n_splits=folds, shuffle=True)

    for train_index, test_index in skf.split(x, y):
            X_train, X_test = x[train_index], x[test_index]
            y_train, y_test = y[train_index], y[test_index]

            model = regressor_model(**params) 

            model.fit(X_train, y_train)
            current_metrics = evaluate(model, (X_test, y_test))

            for metric in current_metrics.keys():
                _metrics[metric].append(current_metrics[metric])
    
    # Averaging metrics
    for metric in _metrics.keys():
        _metrics[metric] = (np.mean(_metrics[metric]), np.std(_metrics[metric]))

    _metrics["folds"] = folds
    _metrics["model"] = model_name
    _metrics["time"] = str(datetime.now())

    write_results(_metrics)
    print(_metrics)



if __name__ == "__main__":
    parser = build_parser()
    args = parser.parse_args()

    model = args.model
    folds = args.folds
    features = COLUMNS

    run_kfold(model, features, folds)