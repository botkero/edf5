lines = []
with open("index.md", "r", encoding="UTF-8") as f:
    lines = f.readlines()

# print(lines)

name = ""
with open("index.md", "w", encoding="UTF-8") as f:
    for line in lines:
        if line.startswith("##"):
            name = line[2:]

        if line.startswith("  [!["):
            name = name.replace("\n", "")
            line = line.replace("Today's schedule", name)

        f.write(line)