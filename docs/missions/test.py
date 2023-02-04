data = []
with open ("index.md", "r") as f:
    data = f.readlines()
    print(data[0])

with open ("index.md", "w") as f:
    for i in range (len(data)):
        d = data[i].replace("-", "")
        f.write(str(i)+ ". " + d)