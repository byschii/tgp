
import numpy as np
from tokenizers import ByteLevelBPETokenizer
from pathlib import Path
import os
import random
from datasets import load_dataset


tokenizer = ByteLevelBPETokenizer("tokenizer/ttookk-vocab.json", "tokenizer/ttookk-merges.txt")
ds = load_dataset("text", data_dir="tokenizer/data")

def encode_with_tokenizer_no_batch(example):
    x = example["text"]
    tok = tokenizer.encode(x).ids
    return {'tok': tok}

def encode_with_tokenizer_batch(example):
    return {
        "tok":
        [tokenizer.encode(x).ids
        for x in example["text"]]
    }
    
ds = ds.map(encode_with_tokenizer_batch, batched=True)

# join 'tok' column without for loop
print("saving train...")
np.concatenate(ds['train']['tok'], dtype=np.int16).tofile(os.path.join(os.path.dirname(__file__), f"train.bin"))

print("saving val.bin")
np.concatenate(ds['validation']['tok'], dtype=np.int16).tofile(os.path.join(os.path.dirname(__file__), f"val.bin"))

# volendo potrei mettere su una riga per evitare di salvare in memoria
# ma non so se è più veloce