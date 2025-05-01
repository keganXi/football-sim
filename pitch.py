# Grid (Pitch)
#
#   0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20 (-1)
#   A   B   C   D   E   F   G   H   I   J   K   L   M   N   O   P   Q   R   S   T   U
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
# 24
# 25
# 26 (-1)
#
# players on the pitch should be 1 or -1, the whole pitch should be 0's, and and player position
# should correspond to pitch coordinates, that how we retrieve the player

import numpy as np
import pandas as pd


COLS, ROWS = 21, 26 # (29, 24)

PITCH = np.zeros((ROWS, COLS))
PITCH = PITCH.astype(int)
PITCH_3rd = int(len(PITCH)/3) # 3rd of the pitch (row)
PITCH_LANE = int(len(PITCH[0])/3) # 3rd of the pitch (col)

GRID = pd.DataFrame(
    PITCH,
    index=[idx for idx in range(ROWS)],
    columns=[idx for idx in range(COLS)]
)

FINAL_THIRD = GRID[:PITCH_3rd] # Attack
MIDDLE_THIRD = GRID[PITCH_3rd:PITCH_3rd*2] # Midfield
DEFENSIVE_THIRD = GRID[PITCH_3rd*2:-1] # Defence

HOME_FINAL_THIRD = FINAL_THIRD
HOME_DEFENSIVE_THIRD = DEFENSIVE_THIRD

AWAY_DEFENSIVE_THIRD = FINAL_THIRD
AWAY_FINAL_THIRD = DEFENSIVE_THIRD
