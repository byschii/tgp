
import os


def get_file_size_MB(file_path):
    return os.path.getsize(file_path) / 1024 / 1024

def clean_page(data:str) -> str:
    # remove excessive \n
    data = data.replace("\n\n", "\n").replace(" .", ". ")
    data = data.replace("...", ".").replace("...", ".")
    data = data.replace("  ", " ")

    # remove lines with less than X characters
    data = data.split("\n")
    data = [line for line in data if len(line) > 100]
    data = "\n".join(data)
    return data



# remove every thing in 'prepared' directory
for file_name in os.listdir(os.path.join(os.path.dirname(__file__), 'prepared')):
    if file_name.endswith(".txt"):
        os.remove(os.path.join(os.path.dirname(__file__), 'prepared', file_name))

qt_page = 10
# read every .txt file in 'test_thesis' directory
for dest_file_index, file_name in enumerate(os.listdir(os.path.join(os.path.dirname(__file__), 'pages'))):
    data = ""
    with open(os.path.join(os.path.dirname(__file__), 'pages', file_name), 'r') as f:
        data += f.read()

    data = clean_page(data)

    # open dest file and write
    dest_filename = "data{}.txt".format(dest_file_index%qt_page)
    with open(os.path.join(os.path.dirname(__file__), 'prepared', dest_filename), 'a+') as f:
        f.write(data)

# read every file in 'prepared' directory
sizes = []
for file_name in os.listdir(os.path.join(os.path.dirname(__file__), 'prepared')):
    extact_filename = os.path.join(os.path.dirname(__file__), 'prepared', file_name)
    sizes.append(int(get_file_size_MB(extact_filename)))
avg_size = sum(sizes)/len(sizes)
circa_in_bg = round(avg_size*qt_page/1024,3)
print("downloaded circa {} GB".format(circa_in_bg))


