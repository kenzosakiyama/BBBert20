from bert_classifier import *
from ekphrasis.classes.preprocessor import TextPreProcessor 
import pandas as pd
from typing import List
from tqdm import tqdm
import re
import torch
from argparse import ArgumentParser

PATH = "/home/kenzo/bbb20/BabuSantana_1p.csv"
MODEL = "/home/kenzo/bbb20/bert_classifier"

parser = ArgumentParser()
parser.add_argument("--file", type=str, required=True,
                    help="Path to the candidate file csv."
                    )
parser.add_argument("--output", type=str, required=True,
                    help="Path to the candidate file csv."
                    )
parser.add_argument("--learner_path", type=str, required=True,
                    help="Path to the learner exported object."
                    )
parser.add_argument("--tokenizer", type=str, required=True,
                    help="Path to the tokenizer."
                    )
parser.add_argument("--labels", type=str, required=True,
                    help="Path to the tabels."
                    )
parser.add_argument("--seq_len", type=int, default=512,
                    help="Maximum sequence length for the model."
                    )
parser.add_argument("--bs", type=int, default=16,
                    help="Batch size for inference."
                    )

parser.add_argument("--gpu",  action='store_true',
                    help="Batch size for inference."
                    )


class CandidateAnalyser:

    def __init__(self, classifier: BertForClassification, file: str, bs: int):
        self.tweet_data = self._get_df(file)
        self.tweet_processor = self._get_text_processor()
        self.cleaned_tweets = self._clean_tweets()
        self.classifier = classifier
        self.bs = bs
    
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

    def get_statistics(self, output_file: str) -> None:
        tweet_dl = self.classifier.prepare_batches(self.cleaned_tweets, self.bs)
        # tweet_dl = self.cleaned_tweets[:1000]
        predictions = self._get_predictions(tweet_dl)

        sentiments = []
        neutral_scores = []
        positive_scores = []
        negative_scores = []

        for prediction in tqdm(predictions, desc= "- Analysing"):
            sentiments.append(prediction[0])
            scores = prediction[1].squeeze()
            neutral_scores.append(scores[0].item())
            positive_scores.append(scores[1].item())
            negative_scores.append(scores[2].item())

        self.tweet_data["sentiment"] = sentiments
        self.tweet_data["negative_score"] = negative_scores
        self.tweet_data["neutral_score"] = neutral_scores
        self.tweet_data["positive_score"] = positive_scores
        
        self.tweet_data.to_csv(output_file, index=False)
        

if __name__ == "__main__":
    args = parser.parse_args()
    learner = load_learner(args.learner_path)
    model = learner.model

    if not args.gpu: model = model.cpu()
    
    tokenizer = BertTokenizer.from_pretrained(args.tokenizer)

    bert = BertForClassification(model, tokenizer, args.seq_len, args.labels, gpu=args.gpu)

    oi = CandidateAnalyser(bert, args.file, args.bs)

    oi.get_statistics(args.output)