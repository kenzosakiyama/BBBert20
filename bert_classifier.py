import os
from tqdm import tqdm
from typing import List
from argparse import ArgumentParser
from transformers import BertForSequenceClassification, BertTokenizer, BertConfig
from fastai import *
from fastai.text import *
from fastai.callbacks import *
import torch
from torch.utils.data import DataLoader, Dataset
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


class InputIDsSequences(Dataset):
    def __init__(self, id_sequences : List[List[int]]):
        self.id_sequences = id_sequences
    
    def __len__(self):
        return len(self.id_sequences)
    
    def __getitem__(self, idx):
        return self.id_sequences[idx]


class BertForClassification():
    def __init__(self, model: nn.Module, tokenizer: BertTokenizer, seq_length: int, path_to_labels: str):
        self.tokenizer = tokenizer
        self.model = model
        self.max_len = seq_length
        self.label_dict = self._get_label_dict(path_to_labels)
        self.softmax = nn.Softmax(dim=0)

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
    
    def prepare_batches(self, text_inputs: List[str], batch_size: int) -> DataLoader:
        id_sequences = []
        # print(text_inputs[:2])
        for sequence in tqdm(text_inputs, desc="- Sequences to encode"):
            encoded_sequence = self.tokenizer.encode(sequence, max_length=self.max_len, add_special_tokens=True, pad_to_max_length=True)
            id_sequences.append(torch.tensor(encoded_sequence))
        
        # print(id_sequences[:3])
        sequences_dl = InputIDsSequences(id_sequences)

        return DataLoader(sequences_dl, batch_size=batch_size)
        # return sequences_dl

    def _convert_outputs_to_scores(self, outputs: torch.tensor) -> (str, torch.tensor):
        classes_and_scores = []

        for output in outputs:
            scores = self.softmax(output, )
            index = scores.argmax().item()

            classes_and_scores.append((self.label_dict[index], scores))
        
        return classes_and_scores

    def predict_on_batches(self, dataloader: DataLoader) -> List[torch.tensor]:
        classes_and_scores = []
        with torch.no_grad():
            for batch in tqdm(dataloader, desc="- Batches to predict"):
                # print(batch.shape)
                outputs = self.model(batch)
                classes_and_scores.extend(self._convert_outputs_to_scores(outputs))
                break
            
        return classes_and_scores

    def predict(self, input_sentence: str) -> (str, torch.tensor):
        encoded_sentence = self._encode(input_sentence)
        tensor_input =  torch.tensor(encoded_sentence).unsqueeze(0)
        output = self.model(tensor_input)
        
        return self._convert_outputs_to_scores([output.squeeze()])[0]
        
        

if __name__ == "__main__":
    args = parser.parse_args()
    learner = load_learner(args.learner_path)
    model = learner.model.cpu()
    tokenizer = BertTokenizer.from_pretrained(args.tokenizer)

    bert = BertForClassification(model, tokenizer, args.seq_len, args.labels)
    teste = bert.prepare_batches(["Eu to feliz", "Eu to muito feliz", "Eu to muito triste"], 2)
    # for i in teste:
    #     print(bert.model(i).shape)
    # print(bert.prepare_batches(["teste1", "teste outro", "mais teste"], 2).shape)
    print(bert.predict_on_batches(teste))
    print("Pronto")
    while True:
        sentence = input()
        print(bert.predict(sentence))