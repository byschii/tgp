# train a miniature character-level shakespeare model
# good for debugging and playing on macbooks and such


out_dir = 'out-model'
eval_interval = 150 # keep frequent because we'll overfit, also checkpointing 
eval_iters = eval_interval
log_interval = 25 # don't print too too often

# we expect to overfit on this small dataset, so only save when val improves
always_save_checkpoint = False

dataset = '../tokenizer'
batch_size = 16

# baby GPT model :)
block_size = 32 # context of up to 256 previous characters (2048 on gpt3)
n_layer = 8
n_head = 16
n_embd = 64*7 # called d_model in gpt3 paper
# block_size / n_heads = head_dimention

dropout = 0.1
learning_rate = 2.5e-4 # with baby networks can afford to go a bit higher
max_iters = eval_interval * 30
lr_decay_iters = max_iters # 1500 # make equal to max_iters usually
min_lr = learning_rate / 23 # 1e-4 # learning_rate / 10 usually
beta2 = 0.9 # make a bit bigger because number of tokens per iter is small

warmup_iters = 100 # not super necessary potentially

"""
lasta run desc
block_size = 20
dropout = 0.1
eval: 5.4069
tok: 20k
---
model3
block_size = 26
dropout = 0.15
eval: 5.2674
tok: 20k
---
block_size = 30
n_head = 32
eval: 4.9
tok: 20k

"""