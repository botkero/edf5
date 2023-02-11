import re
from typing import List
from typing import Tuple

from os import listdir
from os.path import isfile, join

enemies = ['DRAGONSMALL401.SGO', 
    'DRAGONSMALL401_HS.SGO', 
    'E503_ARMORFROG_AF.SGO', 
    'E503_ARMORFROG_AF_LEADER.SGO', 
    'E503_ARMORFROG_LC.SGO', 
    'E503_ARMORFROG_LC_LEADER.SGO', 
    'E503_ARMORFROG_SG.SGO', 
    'E503_ARMORFROG_SG_LEADER.SGO', 
    'E503_FROG_AF.SGO', 
    'E503_FROG_AF_LEADER.SGO', 
    'E503_FROG_LC.SGO', 
    'E503_FROG_LC_LEADER.SGO', 
    'E503_FROG_SG.SGO', 
    'E503_FROG_SG_LEADER.SGO', 
    'E504_MONSTERA.SGO', 
    'E504_MONSTERA_M034_3.SGO', 
    'E505_GENERATOR.SGO', 
    'E505_GENERATORDESTROY.SGO', 
    'E505_GENERATOR_LARGE.SGO', 
    'E505_GENERATOR_LARGE_DESTROY.SGO', 
    'E505_GENERATOR_SUPERLARGE.SGO', 
    'E505_GENERATOR_SUPERLARGE_DESTROY.SGO', 
    'E506_BIGGREY_AF.SGO', 
    'E506_BIGGREY_AF_LEADER.SGO', 
    'E506_BIGGREY_LL.SGO', 
    'E506_BIGGREY_LL_LEADER.SGO', 
    'E506_BIGGREY_SG.SGO', 
    'E506_BIGGREY_SG_LEADER.SGO', 
    'E507_GOLDUFO.SGO', 
    'E507_GOLDUFO_ACE.SGO', 
    'E507_GOLDUFO_BIG.SGO', 
    'E507_GOLDUFO_CHARGE.SGO', 
    'E507_GOLDUFO_HI.SGO', 
    'E508_CARRIER.SGO', 
    'E509_DEIROI.SGO', 
    'E509_DEIROIFOOTPARTS_BEAM.SGO', 
    'E509_DEIROIFOOTPARTS_JOINT.SGO', 
    'E509_DEIROIFOOTPARTS_MISSILE.SGO', 
    'E509_DEIROIFOOTPARTS_ROOT.SGO', 
    'E509_DEIROIFOOTPARTS_TOE.SGO', 
    'E509_DEIROI_FALL.SGO', 
    'E509_DEIROI_FALL_L.SGO', 
    'E509_DEIROI_FALL_M.SGO', 
    'E509_DEIROI_FALL_S.SGO', 
    'E509_DEIROI_FALL_SM.SGO', 
    'E509_DEIROI_FALL_XL.SGO', 
    'E509_DEIROI_L.SGO', 
    'E509_DEIROI_M.SGO', 
    'E509_DEIROI_S.SGO', 
    'E509_DEIROI_SM.SGO', 
    'E509_DEIROI_XL.SGO', 
    'E510_DLC_FORTRESS.SGO', 
    'E510_DLC_FORT_PARTS_LARGECANNON.SGO', 
    'E510_DLC_FORT_PARTS_MEDIUMCANNON.SGO', 
    'E510_DLC_FORT_PARTS_SMALLCANNON1.SGO', 
    'E510_DLC_FORT_PARTS_SMALLCANNON1_AA.SGO', 
    'E510_DLC_FORT_PARTS_SMALLCANNON1_G.SGO', 
    'E510_DLC_FORT_PARTS_SMALLCANNON1_X.SGO', 
    'E510_DLC_FORT_PARTS_SMALLCANNON2.SGO', 
    'E510_DLC_FORT_PARTS_SMALLCANNON2_AA.SGO', 
    'E510_DLC_FORT_PARTS_SMALLCANNON2_X.SGO', 
    'E510_DLC_FORT_PARTS_SMALLCANNON3.SGO', 
    'E510_FORTRESS.SGO', 
    'E510_FORTRESS_DEBRIS1.SGO', 
    'E510_FORTRESS_DEBRIS2.SGO', 
    'E510_FORTRESS_DEBRIS3.SGO', 
    'E510_FORTRESS_DEBRIS4.SGO', 
    'E510_FORTRESS_PARTS_LARGECANNON.SGO', 
    'E510_FORTRESS_PARTS_MEDIUMCANNON.SGO', 
    'E510_FORTRESS_PARTS_SMALLCANNON1.SGO', 
    'E510_FORTRESS_PARTS_SMALLCANNON1_AA.SGO', 
    'E510_FORTRESS_PARTS_SMALLCANNON1_G.SGO', 
    'E510_FORTRESS_PARTS_SMALLCANNON1_X.SGO', 
    'E510_FORTRESS_PARTS_SMALLCANNON2.SGO', 
    'E510_FORTRESS_PARTS_SMALLCANNON2_AA.SGO', 
    'E510_FORTRESS_PARTS_SMALLCANNON2_X.SGO', 
    'E510_FORTRESS_PARTS_SMALLCANNON3.SGO', 
    'E511_MOTHERSHIP.SGO', 
    'E511_MOTHERSHIP_DLC.SGO', 
    'E511_MOTHERSHIP_GENOCIDE_L.SGO', 
    'E511_MOTHERSHIP_GENOCIDE_S.SGO', 
    'E511_MOTHERSHIP_UNIT1.SGO', 
    'E511_MOTHERSHIP_UNIT2.SGO', 
    'E511_MOTHERSHIP_UNIT3.SGO', 
    'E511_MOTHERSHIP_UNIT4.SGO', 
    'E511_MOTHERSHIP_UNIT5.SGO', 
    'E511_MOTHERSHIP_UNIT_SPAWN_EFFECT.SGO', 
    'E513_SHIELDBEARER.SGO', 
    'E513_SHIELDBEARER_FIXED.SGO', 
    'E513_SHIELDBEARER_FIXEDL.SGO', 
    'E513_SHIELDBEARER_FIXEDXL.SGO', 
    'E513_SHIELDBEARER_L.SGO', 
    'E513_SHIELDBEARER_XL.SGO', 
    'E514_DANGO.SGO', 
    'E515_IMPERIALUFO.SGO', 
    'E515_IMPERIALUFO_ACE.SGO', 
    'E516_BIGGREYBOSS.SGO', 
    'E516_BIGGREYBOSS_CENTERMUZZLE.SGO', 
    'E516_BIGGREYBOSS_EFFECTDIVEATTACK.SGO', 
    'E516_BIGGREYBOSS_EFFECTKICKFIRE.SGO', 
    'E516_BIGGREYBOSS_EFFECTLARGE.SGO', 
    'E516_BIGGREYBOSS_EFFECTMIDDLE.SGO', 
    'E516_BIGGREYBOSS_GENOCIDEMUZZLE.SGO', 
    'E516_BIGGREYBOSS_HANDMUZZLE.SGO', 
    'E516_BIGGREYBOSS_METEOR_LARGE.SGO', 
    'E516_BIGGREYBOSS_METEOR_LARGEBREAK.SGO', 
    'E516_BIGGREYBOSS_METEOR_MIDDLE.SGO', 
    'E516_BIGGREYBOSS_METEOR_MIDDLEBREAK.SGO', 
    'E516_BIGGREYBOSS_METEOR_SMALL.SGO', 
    'E516_BIGGREYBOSS_METEOR_SMALLBREAK.SGO', 
    'E516_BIGGREYBOSS_RING.SGO', 
    'E516_BIGGREYBOSS_RING_LARGE.SGO', 
    'E516_BIGGREYBOSS_RING_SMALL.SGO', 
    'E516_GENERATORSPAWNEFFECT.SGO', 
    'E517_ANTHILL.SGO', 
    'ENGINEER.SGO', 
    'GIANTANT01.SGO', 
    'GIANTANT01B.SGO', 
    'GIANTANT01EGG.SGO', 
    'GIANTANT01EGGB.SGO', 
    'GIANTANT01EGG_BREAK.SGO', 
    'GIANTANT01NETLIGHTSYNCMODE.SGO', 
    'GIANTANT02B.SGO', 
    'GIANTANT02BEGG.SGO', 
    'GIANTANT02BEGGB.SGO', 
    'GIANTANT02BEGG_BREAK.SGO', 
    'GIANTANT03B.SGO', 
    'GIANTANT04.SGO', 
    'GIANTANT04SB.SGO', 
    'GIANTANTQUEEN.SGO', 
    'GIANTBEE01.SGO', 
    'GIANTBEE01CHARGE.SGO', 
    'GIANTBEE02CHARGE.SGO', 
    'GIANTBEEQUEEN.SGO', 
    'GIANTBEEQUEEN02.SGO', 
    'GIANTSPIDER01.SGO', 
    'GIANTSPIDER01NETLIGHTSYNCMODE.SGO', 
    'GIANTSPIDERQUEEN.SGO', 
    'GOLDANT.SGO', 
    'GOLDANTEGG.SGO', 
    'GOLDANTEGGB.SGO', 
    'GOLDANTEGG_BREAK.SGO', 
    'GOLDANTQUEEN.SGO', 
    'HEAVYARMOR.SGO', 
    'HORNETNEST401.SGO', 
    'MONSTER501.SGO', 
    'MONSTER501_KING.SGO', 
    'REDSMALLDRAGON.SGO', 
    'REDSMALLDRAGON_HS.SGO', 
    'SHOOTINGTARGET.SGO', 
    'SILVERSPIDER.SGO', 
    'SILVERSPIDERQUEEN.SGO', 
    'YERROWSMALLDRAGON.SGO', 
    'YERROWSMALLDRAGON_HS.SGO'
 ]


def is_location(line: str) -> bool:
    x = re.search(r"location_\d* :", line)
    if x is not None:
        return True
    return False


def any_enemy(line: str) -> bool:
    line = line.lower()

    for enemy in enemies:
        if line.find(enemy.lower()) != -1:
            return True
    return False


def track_lines(line: int, lines: List) -> Tuple[List, int, bool]:

    enemy = False
    code = []
    
    for i in range(line, len(lines)):
        
        if i+1 >= len(lines):
            return [], 0, False

        if any_enemy(lines[i]) and lines[i+1].find("-1") == -1:
            code.append([lines[i], lines[i+1]])
            enemy = True

        if is_location(lines[i]):
            return code, i, enemy


def collect_enemy_phases(lines: List) -> List:
    data = []
    for line in range(len(lines)):

        if is_location(lines[line]):
            code, i, enemy = track_lines(line+1, lines)
            if not bool(code) and i == 0:
                break

            if enemy:
                data.append(code)

            line = i
    
    return data


path = "DEST"
onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]

for file in onlyfiles:
    with open(f"DEST/{file}", "r", encoding="UTF-8") as f:
        lines = f.readlines()

        data = collect_enemy_phases(lines)
        with open(f"DEST_FINAL/{file}", "w", encoding="UTF-8") as ff:
            for d in data:
                for x in d:
                    ff.write(str(x)+"\n")
                ff.write("\n")







# for i in range(10):
#     print(data[i])
#     print()

