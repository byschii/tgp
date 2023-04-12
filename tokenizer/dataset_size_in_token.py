"""
calculate the number of tokens in a dataset
"""

import numpy as np

train_file = "tokenizer/train.bin"
val_file = "tokenizer/val.bin"

on_train = len(np.fromfile(train_file, dtype=np.int16))
on_val = len(np.fromfile(val_file, dtype=np.int16))

print("train size: {} tokens".format(on_train))
print("val size: {} tokens".format(on_val))

print("total size: {}kk tokens".format((on_train+on_val)//1_000_000))


