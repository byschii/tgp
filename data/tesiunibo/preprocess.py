
import os

# read every .txt file in 'test_thesis' directory

data = ""
for file_name in os.listdir(os.path.join(os.path.dirname(__file__), 'test_thesis')):
    if file_name.endswith(".txt"):
        with open(os.path.join(os.path.dirname(__file__), 'test_thesis', file_name), 'r') as f:
            data += f.read()

# remove excessive \n
data = data.replace("\n\n", "\n")
data = data.replace(" .", ".")
data = data.replace("...", ".")
data = data.replace("...", ".")
data = data.replace("  ", " ")




# remove lines with less than 20 characters
data = data.split("\n")
data = [line for line in data if len(line) > 110]
data = "\n".join(data)

DESTINATION = os.path.join(os.path.dirname(__file__), 'prepared', 'data.txt')
with open(DESTINATION, 'w+') as f:
    f.write(data)

    # print size of file
    f.seek(0, os.SEEK_END)
    print("File size: {} kbytes".format(int(f.tell() / 1024)))


