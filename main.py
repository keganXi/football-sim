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
import  json
import time
from passing import POSITION_COORDINATES
from players import HOME_PLAYERS
from scan import scan_pitch


def field_players(side):
    # NOTE: side -> "HOME" or "AWAY"
    num = 1
    if side == "AWAY":
        num = -1
    for key, value in POSITION_COORDINATES.items():
        row = value[side][0]
        col = value[side][1]
        print(f"Position {key}: {PITCH[row][col]}")
        PITCH[row][col] = num


COLS, ROWS = 19, 24 # (19, 24)

PITCH = np.zeros((ROWS, COLS))
PITCH = PITCH.astype(int)

field_players("HOME")
field_players("AWAY")


print(PITCH)
print(f"rows: {len(PITCH)}")
print(f"columns: {len(PITCH[0])}")
print(f"Position: {PITCH[0][4]}") # (-1, 5) -> (row, col)
print("\nScan for passing lanes...")

MINUTE = 0
FULL_TIME = 90

player_position = POSITION_COORDINATES["GK"]["HOME"]
print(player_position)
total_passes = []
while MINUTE < FULL_TIME:
    MINUTE+=1

    player = scan_pitch(PITCH, player_position)
    if player is None:
        print("nothing found")

    get_position = ""
    for key, value in POSITION_COORDINATES.items():
        if value["HOME"] == player:
            get_position = key

    position = ()
    for item in HOME_PLAYERS:
        if item["role"] == get_position:
            print(f"{item["name"]} - {item["role"]}")
    player_position = player

    total_passes.append(MINUTE)
    # time.sleep(1)

print(f"Total Passes {len(total_passes)}")
