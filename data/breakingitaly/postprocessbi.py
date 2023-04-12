
import os

# read every .txt file in this directory

data = ""
for file_name in os.listdir(os.path.dirname(__file__)):
    if file_name.endswith(".txt"):
        with open(os.path.join(os.path.dirname(__file__), file_name), 'r') as f:
            data += f.read()

data = data.replace("\n\n", " ")

# remove a \n every 2
for i in range(0, len(data)):
    if data[i] == "\n" and i % 2 == 0:
        data = data[:i] + " " + data[i+1:]

# remove a \n every 3
for i in range(0, len(data)):
    if data[i] == "\n" and i % 3 == 0:
        data = data[:i] + " " + data[i+1:]

# remove a \n every 4
for i in range(0, len(data)):
    if data[i] == "\n" and i % 4 == 0:
        data = data[:i] + " " + data[i+1:]

# remove a \n every 5
for i in range(0, len(data)):
    if data[i] == "\n" and i % 5 == 0:
        data = data[:i] + " " + data[i+1:]

# remove a \n every 4
for i in range(0, len(data)):
    if data[i] == "\n" and i % 4 == 0:
        data = data[:i] + " " + data[i+1:]

# remove a \n every 3
for i in range(0, len(data)):
    if data[i] == "\n" and i % 3 == 0:
        data = data[:i] + " " + data[i+1:]
        




data = data.replace("  ", " ")

# dave data in 'prepared' directory
with open(os.path.join(os.path.dirname(__file__), 'prepared', 'data.txt'), 'w+') as f:
    f.write(data)


