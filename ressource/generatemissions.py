import json

# all missions pictures (sorted)
base = [
   "(../../images/missions_thumbnails/M000.jpg)",
   "(../../images/missions_thumbnails/M001.jpg)",
   "(../../images/missions_thumbnails/M003.jpg)",
   "(../../images/missions_thumbnails/M004.jpg)",
   "(../../images/missions_thumbnails/M005.jpg)",
   "(../../images/missions_thumbnails/M006.jpg)",
   "(../../images/missions_thumbnails/M006_5.jpg)",
   "(../../images/missions_thumbnails/M009.jpg)",
   "(../../images/missions_thumbnails/M013.jpg)",
   "(../../images/missions_thumbnails/M018.jpg)",
   "(../../images/missions_thumbnails/M015_2.jpg)",
   "(../../images/missions_thumbnails/M008.jpg)",
   "(../../images/missions_thumbnails/M015.jpg)",
   "(../../images/missions_thumbnails/M015_3.jpg)",
   "(../../images/missions_thumbnails/M010.jpg)",
   "(../../images/missions_thumbnails/M011.jpg)",
   "(../../images/missions_thumbnails/M012.jpg)",
   "(../../images/missions_thumbnails/M014.jpg)",
   "(../../images/missions_thumbnails/M016.jpg)",
   "(../../images/missions_thumbnails/M017.jpg)",
   "(../../images/missions_thumbnails/M017_5.jpg)",
   "(../../images/missions_thumbnails/M007.jpg)",
   "(../../images/missions_thumbnails/M024.jpg)",
   "(../../images/missions_thumbnails/M019_5.jpg)",
   "(../../images/missions_thumbnails/M022.jpg)",
   "(../../images/missions_thumbnails/M023.jpg)",
   "(../../images/missions_thumbnails/M025.jpg)",
   "(../../images/missions_thumbnails/M019.jpg)",
   "(../../images/missions_thumbnails/M026.jpg)",
   "(../../images/missions_thumbnails/M020_5.jpg)",
   "(../../images/missions_thumbnails/M021.jpg)",
   "(../../images/missions_thumbnails/M027.jpg)",
   "(../../images/missions_thumbnails/M028.jpg)",
   "(../../images/missions_thumbnails/M029.jpg)",
   "(../../images/missions_thumbnails/M020.jpg)",
   "(../../images/missions_thumbnails/M036.jpg)",
   "(../../images/missions_thumbnails/M032_5.jpg)",
   "(../../images/missions_thumbnails/M034.jpg)",
   "(../../images/missions_thumbnails/M034_3.jpg)",
   "(../../images/missions_thumbnails/M034_5.jpg)",
   "(../../images/missions_thumbnails/M035.jpg)",
   "(../../images/missions_thumbnails/M007_5.jpg)",
   "(../../images/missions_thumbnails/M033.jpg)",
   "(../../images/missions_thumbnails/M037.jpg)",
   "(../../images/missions_thumbnails/M031.jpg)",
   "(../../images/missions_thumbnails/M041.jpg)",
   "(../../images/missions_thumbnails/M042.jpg)",
   "(../../images/missions_thumbnails/M046_1.jpg)",
   "(../../images/missions_thumbnails/M047.jpg)",
   "(../../images/missions_thumbnails/M047_2.jpg)",
   "(../../images/missions_thumbnails/M091.jpg)",
   "(../../images/missions_thumbnails/M056.jpg)",
   "(../../images/missions_thumbnails/M042_2.jpg)",
   "(../../images/missions_thumbnails/M030.jpg)",
   "(../../images/missions_thumbnails/M053.jpg)",
   "(../../images/missions_thumbnails/M203.jpg)",
   "(../../images/missions_thumbnails/M042_5.jpg)",
   "(../../images/missions_thumbnails/M200.jpg)",
   "(../../images/missions_thumbnails/M050.jpg)",
   "(../../images/missions_thumbnails/M038.jpg)",
   "(../../images/missions_thumbnails/M091_2.jpg)",
   "(../../images/missions_thumbnails/M061.jpg)",
   "(../../images/missions_thumbnails/M043.jpg)",
   "(../../images/missions_thumbnails/M058.jpg)",
   "(../../images/missions_thumbnails/M045.jpg)",
   "(../../images/missions_thumbnails/M063_5.jpg)",
   "(../../images/missions_thumbnails/M044.jpg)",
   "(../../images/missions_thumbnails/M065.jpg)",
   "(../../images/missions_thumbnails/M076.jpg)",
   "(../../images/missions_thumbnails/M046_3.jpg)",
   "(../../images/missions_thumbnails/M091_3.jpg)",
   "(../../images/missions_thumbnails/M201.jpg)",
   "(../../images/missions_thumbnails/M051.jpg)",
   "(../../images/missions_thumbnails/M068.jpg)",
   "(../../images/missions_thumbnails/M048.jpg)",
   "(../../images/missions_thumbnails/M202.jpg)",
   "(../../images/missions_thumbnails/M074.jpg)",
   "(../../images/missions_thumbnails/M091_4.jpg)",
   "(../../images/missions_thumbnails/M067.jpg)",
   "(../../images/missions_thumbnails/M072_1.jpg)",
   "(../../images/missions_thumbnails/M072_2.jpg)",
   "(../../images/missions_thumbnails/M072_3.jpg)",
   "(../../images/missions_thumbnails/M072_4.jpg)",
   "(../../images/missions_thumbnails/M064.jpg)",
   "(../../images/missions_thumbnails/M059.jpg)",
   "(../../images/missions_thumbnails/M057.jpg)",
   "(../../images/missions_thumbnails/M063.jpg)",
   "(../../images/missions_thumbnails/M054.jpg)",
   "(../../images/missions_thumbnails/M039.jpg)",
   "(../../images/missions_thumbnails/M049.jpg)",
   "(../../images/missions_thumbnails/M062.jpg)",
   "(../../images/missions_thumbnails/M069.jpg)",
   "(../../images/missions_thumbnails/M055.jpg)",
   "(../../images/missions_thumbnails/M075.jpg)",
   "(../../images/missions_thumbnails/M066.jpg)",
   "(../../images/missions_thumbnails/M073_5.jpg)",
   "(../../images/missions_thumbnails/M054_5.jpg)",
   "(../../images/missions_thumbnails/M046_2.jpg)",
   "(../../images/missions_thumbnails/M204.jpg)",
   "(../../images/missions_thumbnails/M079.jpg)",
   "(../../images/missions_thumbnails/M090.jpg)",
   "(../../images/missions_thumbnails/M052.jpg)",
   "(../../images/missions_thumbnails/M060.jpg)",
   "(../../images/missions_thumbnails/M070.jpg)",
   "(../../images/missions_thumbnails/M078.jpg)",
   "(../../images/missions_thumbnails/M071.jpg)",
   "(../../images/missions_thumbnails/M080.jpg)",
   "(../../images/missions_thumbnails/M081.jpg)",
   "(../../images/missions_thumbnails/M082.jpg)",
   "(../../images/missions_thumbnails/M083.jpg)",
   "(../../images/missions_thumbnails/M098.jpg)",
   "(../../images/missions_thumbnails/M099.jpg)"
]

dlc1 = [
    "(../../images/dlc1/DLC_DM011.jpg)",
    "(../../images/dlc1/DLC_DM013.jpg)",
    "(../../images/dlc1/DLC_DM018.jpg)",
    "(../../images/dlc1/DLC_DM005.jpg)",
    "(../../images/dlc1/DLC_DM019.jpg)",
    "(../../images/dlc1/DLC_DM020.jpg)",
    "(../../images/dlc1/DLC_DM008.jpg)",
    "(../../images/dlc1/DLC_DM003.jpg)",
    "(../../images/dlc1/DLC_DM013.jpg)",
    "(../../images/dlc1/DLC_DM003_2.jpg)",
    "(../../images/dlc1/DLC_DM001.jpg)",
    "(../../images/dlc1/DLC_DM007.jpg)",
    "(../../images/dlc1/DLC_DM003_3.jpg)",
    "(../../images/dlc1/DLC_DM013_2.jpg)",
    "(../../images/dlc1/DLC_DM015.jpg)"
]

dlc2 = [
    "(../../images/dlc2/DLC_DM005_2.jpg)",
    "(../../images/dlc2/DLC_DM002.jpg)",
    "(../../images/dlc2/DLC_DM021.jpg)",
    "(../../images/dlc2/DLC_DM006_2.jpg)",
    "(../../images/dlc2/DLC_DM009.jpg)",
    "(../../images/dlc2/DLC_DM007_2.jpg)",
    "(../../images/dlc2/DLC_DM010.jpg)",
    "(../../images/dlc2/DLC_DM014_2.jpg)",
    "(../../images/dlc2/DLC_DM012.jpg)",
    "(../../images/dlc2/DLC_DM022.jpg)",
    "(../../images/dlc2/DLC_DM023.jpg)",
    "(../../images/dlc2/DLC_DM024.jpg)",
    "(../../images/dlc2/DLC_DM017.jpg)",
    "(../../images/dlc2/DLC_DM016.jpg)"
]


def format_filename(mission: str) -> str:
    return (mission.lower()
                   .replace(" ", "_")
                   .replace(":", "")
                   .replace(".", "")
                   .replace("!", "")
                   .replace(" ", "")
            )

# MISSIONLIST.OFFLINE.TXT.EN.json
# MISSIONLIST.ONLINE.TXT.EN.json
# DLC1_MISSIONLIST.OFFLINE.TXT.EN.json
# DLC2_MISSIONLIST.OFFLINE.TXT.EN.json
mission_list_file = "DLC2_MISSIONLIST.OFFLINE.TXT.EN.json"
with open(f"text/{mission_list_file}", encoding="UTF-8") as f:
    missions = json.load(f)

for counter, mission in enumerate(missions):
    filename = format_filename(mission["value"][0]["value"])

    with open(f"missions/{filename}.md", "w") as f:
        # header
        f.write(f"""# {mission["value"][0]["value"]}\n\n""")

        # image
        f.write("<figure markdown>\n")
        image = f"""![{mission["value"][0]["value"]}]""" + dlc2[counter]
        f.write(image+"\n")
        f.write("</figure>\n\n")

        # mission description
        text = mission["value"][1]["value"].replace("%dq%s", "").replace("%dq%", "")
        f.write(text + "\n")
