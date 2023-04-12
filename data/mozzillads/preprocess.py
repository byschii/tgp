
import os

# read every .txt file in 'test_thesis' directory

data = ""
for file_name in os.listdir(os.path.join(os.path.dirname(__file__), 'talks')):
    if file_name.endswith(".txt"):
        with open(os.path.join(os.path.dirname(__file__), 'talks', file_name), 'r') as f:
            data += f.read()

# remove excessive \n
data = data.replace("\n\n", "\n")
data = data.replace("  ", " ")


# remove lines with less than X characters
data = data.split("\n")
data = [line for line in data if len(line) > 50]
data = "\n".join(data)

DESTINATION = os.path.join(os.path.dirname(__file__), 'prepared', 'data.txt')
with open(DESTINATION, 'w+') as f:
    f.write(data)

    # print size of file
    f.seek(0, os.SEEK_END)
    print("File size: {} kbytes".format(int(f.tell() / 1024)))


