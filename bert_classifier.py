import os
from argparse import ArgumentParser
from transformers import BertForSequenceClassification, BertTokenizer, BertConfig
from fastai import *
from fastai.text import *
from fastai.callbacks import *
import torch
import torch.nn as nn

parser = ArgumentParser()
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


class BertForClassification():
    def __init__(self, model: nn.Module, tokenizer: BertTokenizer, seq_length: int, path_to_labels: str):
        self.tokenizer = tokenizer
        self.model = model
        self.max_len = seq_length
        self.label_dict = self._get_label_dict(path_to_labels)
        self.softmax = nn.Softmax(dim=1)

        self.model.eval()

    def _get_label_dict(self, path: str) -> dict:
        with open(path, "r") as f:
            label_dict = {}
            for i, line in enumerate(f.readlines()):
                label_dict[i] = line.strip("\n")
        
        return label_dict

    def _encode(self, input_string: str) -> list:
        id_list = self.tokenizer.encode(input_string, add_special_tokens=True, max_length=self.max_len)

        return id_list

    
    def _to_json(self, data: List[dict], output_file: str) -> None:
        with open(output_file, "w") as fout:
            json.dump(data, fout, indent=2)
    
    
    def predict(self, input_sentence: str) -> str:
        encoded_sentence = self._encode(input_sentence)
        tensor_input =  torch.tensor(encoded_sentence).unsqueeze(0)
        output = self.model(tensor_input)
        scores = self.softmax(output)

        index = scores.argmax().item()
        
        return self.label_dict[index], scores

if __name__ == "__main__":
    args = parser.parse_args()
    learner = load_learner(args.learner_path)
    model = learner.model.cpu()
    tokenizer = BertTokenizer.from_pretrained(args.tokenizer)

    bert = BertForClassification(model, tokenizer, args.seq_len, args.labels)
    
    print("Pronto")
    while True:
        sentence = input()
        print(bert.predict(sentence))