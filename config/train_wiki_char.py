# train a miniature character-level shakespeare model
# good for debugging and playing on macbooks and such


out_dir = 'out-wikisecond'
eval_interval = 100 # keep frequent because we'll overfit, also checkpointing 
eval_iters = 100
log_interval = 25 # don't print too too often

# we expect to overfit on this small dataset, so only save when val improves
always_save_checkpoint = False

wandb_log = False # override via command line if you like
wandb_project = 'tinydante-char'
wandb_run_name = 'mini-gpt'

dataset = 'wikisecond'
batch_size = 16

# baby GPT model :)
block_size = 63 # context of up to 256 previous characters (2048 on gpt3)
n_layer = 10
n_head = 16
n_embd = 128 # called d_model in gpt3 paper
# block_size / n_heads = head_dimention

dropout = 0.2
learning_rate = 5e-4 # with baby networks can afford to go a bit higher
max_iters = 3000
lr_decay_iters = 3000 # make equal to max_iters usually
min_lr = 1e-4 # learning_rate / 10 usually
beta2 = 0.99 # make a bit bigger because number of tokens per iter is small

warmup_iters = 100 # not super necessary potentially

