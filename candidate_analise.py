from bert_classifier import *
from ekphrasis.classes.preprocessor import TextPreProcessor 
import pandas as pd
from typing import List
from tqdm import tqdm
import re
import torch

PATH = "/data/lucasrodrigues/tweets/BabuSantana_1p.csv"


class CandidateAnalyser:

    def __init__(self, classifier: BertForClassification, file: str):
        self.tweet_data = self._get_df(file)
        self.tweet_processor = self._get_text_processor()
        self.cleaned_tweets = self._clean_tweets()
        self.classifier = classifier
    
    def _get_text_processor(self):
        # Text TextPreProcessor
        text_processor = TextPreProcessor(
            omit=['url', 'email', 'percent', 'money', 'phone', 'user', 'time', 'date', 'number', 'hashtag'],
            normalize=['url', 'email', 'percent', 'money', 'phone', 'user', 'time', 'date', 'number', 'hashtag'],
            fix_html=True,
            segmenter="twitter",
            corrector="twitter",
            unpack_hashtags=False,
            unpack_contractions=False,
            spell_correct_elong=True
        )
        return text_processor


    def _get_df(self, file: str) -> pd.DataFrame:
        return pd.read_csv(file)
    
    def _clean_tweets(self) -> List[str]:
        cleaned_tweets = []

        for tweet in tqdm(self.tweet_data["tweet"].astype(str), desc="- Cleaning tweets"):
            cleaned_tweets.append(self.tweet_processor.pre_process_doc(tweet))
        
        return cleaned_tweets
    
    def get_statistics(self):
        tweet_dl = self.classifier.prepare_batches(self.cleaned_tweets)

        for batch in tqdm(tweet_dl):
            print()self.classifier.predict_on_batches(batch)
