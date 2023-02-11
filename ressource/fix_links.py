from os import listdir
from os.path import isfile, join

path = "."
onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]


# print(onlyfiles)
for file in onlyfiles:
    lines = []
    with open(file, "r", encoding="UTF-8") as f:
        lines = f.readlines()

    with open(file, "w", encoding="UTF-8") as f:
        for line in lines:
            if line.startswith("!["):
                line = line.replace("![", "  ![")
                line = line.replace("../", "../../")
            f.write(line)