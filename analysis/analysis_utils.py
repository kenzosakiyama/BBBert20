from typing import List, Dict
import pandas as pd 
import json

def get_raw_quantities(candidates: List[pd.DataFrame]) -> pd.DataFrame:

    statistics = {"nome": [], "positivos": [], "neutros": [], "negativos": []}

    for name in candidates.keys():
        current_df = candidates[name]
        statistics["nome"].append(name)
        statistics["positivos"].append((current_df["sentiment"] == "Positivo").sum())
        statistics["neutros"].append((current_df["sentiment"] == "Neutro").sum())
        statistics["negativos"].append((current_df["sentiment"] == "Negativo").sum())

    return pd.DataFrame.from_dict(statistics).set_index("nome")

def get_pct_by_candidate(candidates: List[pd.DataFrame]) -> pd.DataFrame:

    raw_quantities = get_raw_quantities(candidates)
    tweets_per_candidate = []

    for candidate in candidates.keys():
        qtd = len(candidates[candidate])
        tweets_per_candidate.append(qtd)
    
    return raw_quantities.div(tweets_per_candidate, axis=0)

def load_json(file: str) -> dict:

    with open(file, "r") as f:
        loaded_json = json.load(f)
    
    return loaded_json

def get_paredoes_info() -> dict:

    return load_json("../infos/paredoes_info.json")

def get_participantes_info() -> dict:

    return load_json("../infos/participantes_info.json")

def get_likes_count(cand_df: pd.DataFrame) -> int:
    
    return cand_df["likes_count"].sum()

def get_retweets_count(cand_df: pd.DataFrame) -> int:
    
    return cand_df["retweets_count"].sum()

def get_tweets_by_day(cand_df: pd.DataFrame, cand_name: str) -> pd.DataFrame:
    
    cand_df["date"] = pd.to_datetime(cand_df["date"])

    days = cand_df["date"].dt.day.unique()
    days.sort()

    day_info = {}

    for i, day in enumerate(days):
        day_info[f"day{i+1}"] = (cand_df["date"].dt.day == day).sum()

    return pd.DataFrame(day_info, index=[cand_name])

def get_hashtags(df: pd.DataFrame) -> pd.DataFrame:
    "Função para extrair hashtags de uma coluna com strings no formato: '['hashtag1', 'hashtag2']' "

    all_hashtags = []
    for i in range(len(df)):
        raw = df["hashtags"].iloc[i][1:-1]
        if len(raw)  == 0: continue
        hashtags = [tag_to_clean.strip()[1:-1] for tag_to_clean in raw.split(",")]
        
        all_hashtags.extend(hashtags)

    hashtags_df = pd.DataFrame(all_hashtags, columns=["hashtag"])
    return hashtags_df


def get_unique_hashtags(candidates: List[pd.DataFrame]) -> pd.DataFrame:

    hashtags_df = pd.DataFrame(columns=["hashtag"])
    for candidate in candidates:
        hashtags_df = hashtags_df.append(get_hashtags(candidate), ignore_index=True)

    hashtag_count = {}

    for hashtag in hashtags_df["hashtag"].unique().tolist():
        hashtag_count[hashtag] = (hashtags_df["hashtag"] == hashtag).sum()

    unique_hashtags_df = pd.DataFrame(hashtag_count.values(), index=hashtag_count.keys(), columns=["quantidade"])

    return unique_hashtags_df

def get_fica_fora_quantities(unique_hashtags_df: pd.DataFrame, alias: Dict[str, str]) -> pd.DataFrame:
    # Alias serão usados para construir as consultas do número de hashtags fica# e fora#
    fica_fora_df = pd.DataFrame(index=alias.keys(), columns=["fica", "fora"])

    for candidate in alias.keys():
        fica_fora_df.loc[candidate]["fica"] = unique_hashtags_df.loc[f"#fica{alias[candidate]}"]["quantidade"]
        fica_fora_df.loc[candidate]["fora"] = unique_hashtags_df.loc[f"#fora{alias[candidate]}"]["quantidade"]
    
    return fica_fora_df


if __name__ == "__main__":
    pass