from argparse import ArgumentParser
from typing import List, Tuple, Dict
from sklearn.model_selection import KFold, GridSearchCV
import pandas as pd 
import numpy as np 
import json
import os

from model_utils import *
from tqdm import tqdm
from sklearn.metrics import make_scorer
from sklearn.linear_model import LinearRegression, SGDRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import AdaBoostRegressor, RandomForestRegressor
from sklearn.svm import SVR

def build_parser() -> ArgumentParser:
    
    parser = ArgumentParser()

    parser.add_argument("--model", required=True, type=str)
    parser.add_argument("--parameters", required=True, type=str, help="Path to a JSON file with the parameters.")
    
    parser.add_argument("--folds", type=int, default=10)
    parser.add_argument("--n_jobs", type=int, default=3)


    return parser

def load_json(path: str) -> Dict:

    with open(path, "r") as f:
        parameters = json.load(f)
    
    return parameters

def setup_scorers() -> List:

    scorers = {metric: make_scorer(METRICS[metric], greater_is_better=False) for metric in METRICS.keys()}
    return scorers

def run_grid_search(model, name: str, parameters: Dict, folds: int, normalize: bool, n_jobs: int, features: List[str]) -> None:
    
    data_df = get_data(features, normalize=normalize)

    x, y = data_df.drop(columns=["paredao", "nome", "rejeicao"], axis=1).to_numpy(), data_df.drop(columns=data_df.columns[:-1], axis=1).to_numpy()
    y = np.ravel(y)

    scorers = setup_scorers()
    gs = GridSearchCV(model, param_grid=parameters, verbose=10, iid=False, cv=folds, refit='mse', scoring=scorers, n_jobs=n_jobs)
    gs.fit(x, y)
    print(data_df.columns.to_list())
    pd.DataFrame(gs.cv_results_).to_csv("grid_search_results/"  + name + "_grid_search_results.csv")

if __name__ == "__main__":
    parser = build_parser()
    args = parser.parse_args()

    model = MODELS[args.model]()
    normalize = NORMALIZE[args.model]
    folds = args.folds
    jobs = args.n_jobs


    parameters = load_json(args.parameters)
    #parameters = {
    # "base_estimator": [SVR(**PARAMETERS["svr"])],
    # "n_estimators": [2,3,4,5,6,7,8,9,10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
    #}

    # features = load_json(args.features)
    features = COLUMNS



    run_grid_search(model, args.model,  parameters, folds,  normalize, jobs, features)
