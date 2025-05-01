# Grid (Pitch)
#
#   0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19 (-1)
#   A   B   C   D   E   F   G   H   I   J   K   L   M   N   O   P   Q   R   S   T
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12
# 13
# 14
# 15
# 16
# 17
# 18
# 19
# 20
# 21
# 22
# 23
# 24 (-1)
#
# players on the pitch should be 1 or -1, the whole pitch should be 0's, and and player position
# should correspond to pitch coordinates, that how we retrieve the player

import numpy as np
import pandas as pd
import  json
import time
from passing import POSITION_COORDINATES, get_passing_lane_and_path
from players import HOME_PLAYERS, AWAY_PLAYERS
from scan import scan_pitch
from possession import in_possession
from awareness import team_awareness


def field_players(side):
    # NOTE: side -> "HOME" or "AWAY"
    num = 1
    PLAYERS = HOME_PLAYERS
    if side == "AWAY":
        PLAYERS = AWAY_PLAYERS
        num = -1

    for role, value in POSITION_COORDINATES.items():
        for player in PLAYERS:
            if player["role"] == role:
                row = value[side][0]
                col = value[side][1]
                PITCH[row, col] = num


COLS, ROWS = 19, 24 # (19, 24)

PITCH = np.zeros((ROWS, COLS))
PITCH = PITCH.astype(int)

df = pd.DataFrame(
    PITCH,
    index=[idx for idx in range(ROWS)],
    columns=[idx for idx in range(COLS)]
)

field_players("HOME")
field_players("AWAY")


print(df)
print(f"rows: {len(PITCH)}")
print(f"columns: {len(PITCH[0])}")
print(f"Position: {PITCH[0][4]}") # (-1, 5) -> (row, col)
print("\nScan for passing lanes...")

MINUTE = 0
FULL_TIME = 90

player_position = POSITION_COORDINATES["LCB"]["HOME"]
BALL_POS = player_position

# print(player_position)
total_passes = []
while MINUTE < FULL_TIME:
    MINUTE+=1

    # scan pitch
    scan = scan_pitch(PITCH, player_position)
    if scan is None:
        print("nothing found")
    check_scan = scan if scan != None else {}
    player = check_scan["player"] # player coordinates
    BALL_POS = check_scan["path"][-1] # e.g [(1,2), (0,3), (2,1)] (0 idx from player, -1 idx current player)

    possess = in_possession(PITCH, BALL_POS)
    team_awareness(PITCH, possess["team"], possess["pos"], BALL_POS)

    print(f"{possess['team']} |\t{possess['name']} - {possess['pos']}")
    player_position = player

    total_passes.append(MINUTE)
    # time.sleep(1)

print(df)
print(f"Total Passes {len(total_passes)}")
