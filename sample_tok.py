"""
Sample from a trained model
"""
import os
import pickle
from contextlib import nullcontext
import torch
import numpy as np
import random
from model import GPTConfig, GPT
import time 
from tokenizers import ByteLevelBPETokenizer
from llm_watermarker import WatermarkBase, SimpleWatermarkDetector, LLMWatermarker
import os


# -----------------------------------------------------------------------------
init_from = 'resume' # either 'resume' (from an out_dir) or a gpt2 variant (e.g. 'gpt2-xl')
out_dir = 'out' # ignored if init_from is not 'resume'
start = "\n" # or "<|endoftext|>" or etc. Can also specify a file, use as: "FILE:prompt.txt"
num_samples = 2 # number of samples to draw
max_new_tokens = 50 # number of tokens generated in each sample
temperature = 0.7 # 1.0 = no change, < 1.0 = less random, > 1.0 = more random, in predictions bigger as model gets better
top_k = 100 # retain only the top_k most likely tokens, clamp others to have 0 probability
seed = random.randint(1,9999) # 1337
device = 'cpu' # examples: 'cpu', 'cuda', 'cuda:0', 'cuda:1', etc.
dtype = 'bfloat16' # 'float32' or 'bfloat16' or 'float16'
compile = False # use PyTorch 2.0 to compile the model to be faster
ckpt_file='ckpt.pt' # checkpoint file name
add_watermark=False # add a watermark to the generated text
exec(open('configurator.py').read()) # overrides from command line or config file
# -----------------------------------------------------------------------------

torch.manual_seed(seed)
torch.cuda.manual_seed(seed)
torch.backends.cuda.matmul.allow_tf32 = True # allow tf32 on matmul
torch.backends.cudnn.allow_tf32 = True # allow tf32 on cudnn
device_type = 'cuda' if 'cuda' in device else 'cpu' # for later use in torch.autocast
ptdtype = {'float32': torch.float32, 'bfloat16': torch.bfloat16, 'float16': torch.float16}[dtype]
ctx = nullcontext() if device_type == 'cpu' else torch.amp.autocast(device_type=device_type, dtype=ptdtype)

# model
if init_from == 'resume':
    # init from a model saved in a specific directory
    ckpt_path = os.path.join(out_dir, ckpt_file)
    checkpoint = torch.load(ckpt_path, map_location=device)
    gptconf = GPTConfig(**checkpoint['model_args'])
    model = GPT(gptconf)
    state_dict = checkpoint['model']
    unwanted_prefix = '_orig_mod.'
    for k,v in list(state_dict.items()):
        if k.startswith(unwanted_prefix):
            state_dict[k[len(unwanted_prefix):]] = state_dict.pop(k)
    model.load_state_dict(state_dict)


model.eval()
model.to(device)
if compile:
    model = torch.compile(model) # requires PyTorch 2.0 (optional)


print("No meta.pkl found, assuming CUSTOM tokenizer...")
tokenizer = ByteLevelBPETokenizer("tokenizer/ttookk-vocab.json", "tokenizer/ttookk-merges.txt")
encode = lambda s: np.array(tokenizer.encode(s).ids)
decode = lambda l: tokenizer.decode(l)

# encode the beginning of the prompt
if start.startswith('FILE:'):
    with open(start[5:], 'r', encoding='utf-8') as f:
        start = f.read()
start_ids = encode(start)
x = (torch.tensor(start_ids, dtype=torch.long, device=device)[None, ...])

watermarker = None
if add_watermark:
    watermarker = None # LLMWatermarker(vocab = tokenizer.get_vocab(), device=device)
    watermarker_verifier = SimpleWatermarkDetector(vocab = tokenizer.get_vocab(), device=device)
    num_samples = 1


# run generation
with torch.no_grad():
    with ctx:
        for k in range(num_samples):
            y = model.generate(x, max_new_tokens, temperature=temperature, top_k=top_k, watermarker=watermarker)
            completion = decode(y[0].tolist())
            print(completion)
            print('\n---------------')

            if add_watermark:
                print("Verifying watermark...")
                tokenized_text = tokenizer.encode(completion).ids
                completion_stats =  watermarker_verifier.score_sequence(tokenized_text)
                print("green_fraction", ">>", completion_stats['green_fraction'])