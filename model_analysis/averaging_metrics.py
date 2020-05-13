import numpy as np 
import json
import pandas as pd 
from typing import List, Dict

METRICS = [
    "mse",
    "mae",
    "r2"
]

def load_json() -> List[Dict]:

    with open("kfold_results.json", "r") as f:
        metrics = json.load(f)
    
    return metrics

def average(executions: List) -> Dict:
    model_name = executions[0]["model"]
    n_executions = len(executions)
    metrics = {name: np.zeros((n_executions, 2)) for name in METRICS}

    infos = {"model": model_name}
    for i, execution in enumerate(executions):
        for metric in METRICS:
            metrics[metric][i] = execution[metric]

    print(f"- Model: {model_name}, with {n_executions}")
    for metric in METRICS:
        values = metrics[metric]
        mean = np.mean(values[:, 0])
        std = np.mean(values[:, 1])
        infos[metric + "_mean"] = np.around(mean, 3)
        infos[metric + "_std"] = np.around(std, 3)

    infos["repetitions"] = n_executions

    return infos

def iterate(metrics: List) -> None:

    columns = ['model', 'mse_mean', 'mse_std', 'mae_mean', 'mae_std', 'r2_mean', 'r2_std', 'repetitions']
    metrics_df = pd.DataFrame(columns=columns)

    current_execution = [metrics[0]]
    current_model = metrics[0]["model"]

    for execution in metrics[1:]:

        if execution["model"] != current_model:
            metrics_df = metrics_df.append(average(current_execution), ignore_index=True)
            current_execution = [execution]
            current_model = execution["model"]
        
        else:
            current_execution.append(execution)

    if len(current_execution) > 0:
        metrics_df = metrics_df.append(average(current_execution), ignore_index=True)
    
    metrics_df.sort_values(by="mse_mean", inplace=True, ascending=False)
    metrics_df.set_index("model", inplace=True)
    
    print(metrics_df)
    metrics_df.to_csv("metrics.csv")

if __name__ == "__main__":
    metrics = load_json()
    iterate(metrics)
    pass