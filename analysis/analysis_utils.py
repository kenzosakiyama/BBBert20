from typing import List
import pandas as pd 

def get_raw_quantities(candidates: List[pd.DataFrame]):

    statistics = {"nome": [], "positivos": [], "neutros": [], "negativos": []}

    for name in candidates.keys():
        current_df = candidates[name]
        statistics["nome"].append(name)
        statistics["positivos"].append((current_df["sentiment"] == "Positivo").sum())
        statistics["neutros"].append((current_df["sentiment"] == "Neutro").sum())
        statistics["negativos"].append((current_df["sentiment"] == "Negativo").sum())

    return pd.DataFrame.from_dict(statistics).set_index("nome")

def get_pct_by_candidate(candidates: List[pd.DataFrame]):

    raw_quantities = get_raw_quantities(candidates)
    tweets_per_candidate = []

    for candidate in candidates.keys():
        qtd = len(candidates[candidate])
        tweets_per_candidate.append(qtd)
    
    return raw_quantities.div(tweets_per_candidate, axis=0)

if __name__ == "__main__":
    pass