# train a miniature character-level shakespeare model
# good for debugging and playing on macbooks and such


out_dir = 'out-wikisecond-tok'
eval_interval = 50 # keep frequent because we'll overfit, also checkpointing 
eval_iters = 100
log_interval = 10 # don't print too too often

# we expect to overfit on this small dataset, so only save when val improves
always_save_checkpoint = False

dataset = '../tokenizer'
batch_size = 32

# baby GPT model :)
block_size = 32 # context of up to 256 previous characters (2048 on gpt3)
n_layer = 12
n_head = 64
n_embd = 256*2 # called d_model in gpt3 paper
# block_size / n_heads = head_dimention

dropout = 0.15
learning_rate = 8e-4 # with baby networks can afford to go a bit higher
max_iters = 2000
lr_decay_iters = max_iters # 1500 # make equal to max_iters usually
min_lr = learning_rate / 10 # 1e-4 # learning_rate / 10 usually
beta2 = 0.99 # make a bit bigger because number of tokens per iter is small

warmup_iters = 100 # not super necessary potentially

