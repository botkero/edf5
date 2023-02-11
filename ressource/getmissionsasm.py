import os
import sys
from os import listdir
from os.path import isdir, join
from os import rename
import shutil

mypath = "."
onlydir = [f for f in listdir(mypath) if isdir(join(mypath, f))]
print(onlydir)


for dir in onlydir:
    if not dir.startswith("M0"):
        continue
    os.system(f"mission_tools_1.62.exe {dir}/MISSION.BVM")

    shutil.copyfile(f"{dir}/MISSION.asm", "DEST/MISSION.asm")
    rename("DEST/MISSION.asm", f"DEST/MISSION_{dir}.asm")
