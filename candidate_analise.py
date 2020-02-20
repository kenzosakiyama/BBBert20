from bert_classifier import *
from ekphrasis.classes.preprocessor import TextPreProcessor 
import pandas as pd
from typing import List
from tqdm import tqdm
import re
import torch

PATH = "/data/lucasrodrigues/tweets/BabuSantana_1p.csv"
MODEL = "../../bert_classifier"


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
    
    def _get_predictions(self, tweet_dl: DataLoader) -> List[tuple]:

        # predictions = []

        predictions = self.classifier.predict_on_batches(tweet_dl)
            
        return predictions

    def get_statistics(self):
        tweet_dl = self.classifier.prepare_batches(self.cleaned_tweets, 32)
        # tweet_dl = self.cleaned_tweets[:1000]
        predictions = self._get_predictions(tweet_dl)


        #TODO: adicionar uma coluna de estatiscas la
        

if __name__ == "__main__":

    learner = load_learner(MODEL)
    model = learner.model.cpu()
    tokenizer = BertTokenizer.from_pretrained("neuralmind/bert-base-portuguese-cased")

    bert = BertForClassification(model, tokenizer, 512, "labels.txt")

    oi = CandidateAnalyser(bert, PATH)

    oi.get_statistics()