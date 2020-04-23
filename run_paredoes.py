from argparse import ArgumentParser
from typing import List, Tuple, Dict
from sklearn.model_selection import KFold, GridSearchCV
import pandas as pd 
import numpy as np 
import os
import json
from regression.regression_utils import *
from model_analysis.model_utils import *

from datetime import datetime
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import AdaBoostRegressor, RandomForestRegressor
from sklearn.svm import SVR
from sklearn.base import clone

NORMALIZE = {
    "linear_regression": True,
    "svm": True,
    "ada_boost": False,
    "random_forest": False,
    "knn": True
}

def run_paredoes() -> None:
    global PATH_TO_DATA

    PATH_TO_DATA = "analysis/data/"
    paredoes = len(os.listdir("analysis/data"))
    for model in MODELS.keys():
        regressor = clone(MODELS[model])
        count = 0
        print(f"- Model: {model}")
        for paredao in range(1, paredoes+1):
            if NORMALIZE[model]:
                train_df, test_df, mean, std = get_train_test(paredao, normalize=True, drop_columns=REMOVE)
            else:
                train_df, test_df = get_train_test(paredao, normalize=False, drop_columns=REMOVE)

            x_train, y_train = train_df.drop(columns=["paredao", "nome", "rejeicao"], axis=1).to_numpy(), train_df.drop(columns=train_df.columns[:-1], axis=1).to_numpy()
            x_test, y_test = test_df.drop(columns=["paredao", "nome", "rejeicao"], axis=1).to_numpy(), test_df.drop(columns=train_df.columns[:-1], axis=1).to_numpy()

            y_train, y_test = np.ravel(y_train), np.ravel(y_test)

            regressor.fit(x_train, y_train)
            prediction = regressor.predict(x_test)

            if NORMALIZE[model]:
                test_df["predicao"] = prediction * std + mean
                test_df["rejeicao"] =  test_df["rejeicao"] * std + mean
            else:
                test_df["predicao"] = prediction
            
            pred_elimination = test_df.sort_values(by="predicao", ascending=False).iloc[0].nome
            true_elimination = test_df.sort_values(by="rejeicao", ascending=False).iloc[0].nome

            if paredao == 6:
                print(test_df.sort_values(by="predicao", ascending=False))
                

            count += 1 if pred_elimination == true_elimination else 0
            print(f"{paredao}-- Eliminado:{true_elimination}, predito: {pred_elimination}")

        print(f"\t- {count}/{paredoes} acertos")
        print()

if __name__ == "__main__":
    run_paredoes()