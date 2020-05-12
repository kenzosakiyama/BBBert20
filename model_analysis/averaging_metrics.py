import numpy as np 
import json
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

def average(executions: List) -> None:
    model_name = executions[0]["model"]
    n_executions = len(executions)
    metrics = {name: np.zeros((n_executions, 2)) for name in METRICS}
    # mse = np.zeros((n_executions, 2))
    # mae = np.zeros((n_executions, 2))
    # r2 = np.zeros((n_executions, 2))
    # print(executions)
    # print(len(executions))
    # print()
    for i, execution in enumerate(executions):
        for metric in METRICS:
            metrics[metric][i] = execution[metric]

    print(f"- Model: {model_name}, with {n_executions}")
    for metric in METRICS:
        values = metrics[metric]
        print(f"\t metric: {metric} -> {np.mean(values[:, 0])} +/- {np.mean(values[:, 1])}")
    # print(metrics["mse"].shape)
    # print(metrics["mae"].shape)
    # print(metrics["r2"].shape)
    print()

def iterate(metrics: List) -> None:

    current_execution = [metrics[0]]
    current_model = metrics[0]["model"]

    for execution in metrics[1:]:

        if execution["model"] != current_model:
            average(current_execution)
            current_execution = [execution]
            current_model = execution["model"]
        
        else:
            current_execution.append(execution)

    if len(current_execution) > 0:
        average(current_execution)

if __name__ == "__main__":
    metrics = load_json()
    iterate(metrics)
    pass