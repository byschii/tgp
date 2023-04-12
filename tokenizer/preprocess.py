import specials_to_remove
from pathlib import Path
import os
import numpy as np

data_path = [
    "data/wikithird/prepared",
    "data/tesiunibo/prepared",
    "data/ilpostscrape/prepared",
    "data/openscrape/prepared",
    "data/immensola/prepared",
    "data/mozzillads/prepared",
]

train_val_split = 0.85
dest_path = "data"
dest_train = "train.txt"
dest_val = "val.txt"
read_size = 2048 * 32 * 2

# delete old files
if os.path.exists(os.path.join(os.path.dirname(__file__), dest_path, dest_train)):
    os.remove(os.path.join(os.path.dirname(__file__), dest_path, dest_train))

if os.path.exists(os.path.join(os.path.dirname(__file__), dest_path, dest_val)):
    os.remove(os.path.join(os.path.dirname(__file__), dest_path, dest_val))

paths = []
for curr_data_path in data_path:
    paths += [str(x) for x in Path(curr_data_path).glob("**/*.txt")]

# print all files
for p in paths:
    print(p)

# read every file
for page_name in paths:
    print(f"Reading {page_name}...")
    with open(page_name, 'r') as p:
        while True:
            read_data = p.read(read_size)
            if not read_data:
                break
            # remove special characters
            for special in specials_to_remove.CHAR_CONVERSION_DICT.items():
                read_data = read_data.replace(special[0], special[1])

            # randomly save in train or val
            if np.random.rand() < train_val_split:
                #print(f"Saving in {dest_train}...")
                with open(os.path.join(os.path.dirname(__file__), dest_path,  dest_train), 'a+') as f:
                    f.write(read_data)
            else:
                #print(f"Saving in {dest_val}...")
                with open(os.path.join(os.path.dirname(__file__), dest_path, dest_val), 'a+') as f:
                    f.write(read_data)                    

            
