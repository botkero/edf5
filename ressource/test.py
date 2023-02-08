
f = open("index.md", "r")
content = f.readlines()
f.close()

for line in content:
    if line.find(".off-glb") != -1:
        print(line.replace("\n",""))
