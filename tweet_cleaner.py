from ekphrasis.classes.preprocessor import TextPreProcessor 
from typing import List, Iterable
from tqdm import tqdm

class TweetCleaner:

    # TODO: Add more OO

    def __init__(self, omit: List[str], normalize: List[str]):
        self.processor = self._get_text_processor()

    def _get_text_processor(self, omit: List[str], normalize: List[str]):
        # Text TextPreProcessor
        text_processor = TextPreProcessor(
            omit=omit,
            normalize=normalize,
            fix_html=True,
            segmenter="twitter",
            corrector="twitter",
            unpack_hashtags=False,
            unpack_contractions=False,
            spell_correct_elong=True
        )
        return text_processor
    
    def clean_tweets(self, tweets: Iterable[str]) -> List[str]:
        cleaned_tweets = []

        for tweet in tqdm(tweets, desc="- Cleaning tweets"):
            cleaned_tweets.append(self.processor.pre_process_doc(tweet))
        
        return cleaned_tweets