
from tokenizers import ByteLevelBPETokenizer
from pathlib import Path
import os
import numpy as np





paths = [str(x) for x in Path("tokenizer/data").glob("**/*.txt")]

tokenizer = ByteLevelBPETokenizer()
tokenizer.train(files=paths, vocab_size=32_000, min_frequency=6)

tokenizer.save_model("./tokenizer", "ttookk")

print(
    tokenizer.encode("Ciao Mondo!").ids,
    "----",
    tokenizer.encode("Ciao Mondo!").tokens,
)

#print(tokenizer.get_vocab())
