# train a miniature character-level shakespeare model
# good for debugging and playing on macbooks and such

device='cpu'
compile=False 

out_dir = 'out-dante-char'
eval_interval = 25 # keep frequent because we'll overfit, also checkpointing 
eval_iters = 100
log_interval = 5 # don't print too too often

# we expect to overfit on this small dataset, so only save when val improves
always_save_checkpoint = False

wandb_log = False # override via command line if you like
wandb_project = 'tinydante-char'
wandb_run_name = 'mini-gpt'

dataset = 'tinydante_char'
batch_size = 16
block_size = 64 # context of up to 256 previous characters

# baby GPT model :)
n_layer = 10
n_head = 16
n_embd = 128
dropout = 0.1

learning_rate = 1e-3 # with baby networks can afford to go a bit higher
max_iters = 800
lr_decay_iters = 800 # make equal to max_iters usually
min_lr = 1e-4 # learning_rate / 10 usually
beta2 = 0.99 # make a bit bigger because number of tokens per iter is small

warmup_iters = 100 # not super necessary potentially

