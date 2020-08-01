import tweepy
import json
import os
from argparse import ArgumentParser
from dotenv import load_dotenv
from datetime import datetime
from copy import deepcopy

parser = ArgumentParser()
parser.add_argument("--credentials_folder", type=str, required=True)
args = parser.parse_args()

dotenv_path = os.path.join(os.path.dirname(args.credentials_folder), '.env')
load_dotenv(dotenv_path)

consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

if __name__ == "__main__":

    with open("participantes_info.json", "r") as f:
        participantes_info = json.load(f)
    
    last_info = deepcopy(participantes_info[-1])
    participantes_info.append(last_info)
    last_info["date"] = str(datetime.now())
    update_info= last_info["infos"]

    for participante in update_info.keys():
        user = update_info[participante]["conta"]
        user_info = api.get_user(user)
        followers = user_info.followers_count
        print(f"Participante {user}, seguidores: {followers}")
        update_info[participante]["seguidores"] = followers 
    
    with open("participantes_info.json", "w") as fout:
        json.dump(participantes_info, fout, indent=2)