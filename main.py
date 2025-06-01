# Grid (Pitch)
#
#   0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20   (-1)
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

from passing import POSITION_COORDINATES, get_passing_lane_and_path
from players import HOME_PLAYERS, AWAY_PLAYERS
from scan import scan_pitch
import numpy as np
from display import display
import matplotlib.pyplot as plt
from matplotlib import colors
from possession import in_possession
from positioning import team_reposition
from pitch import AWAY_6_YARD_BOX, GRID, HOME_6_YARD_BOX, PITCH, PITCH_LANE, PITCH_3rd, HOME_FINAL_THIRD, COLS, ROWS


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
                # get position row/col coordinates
                row = value[side][0]
                col = value[side][1]
                # assign position coordinates to player
                player["coord"] = (row, col)
                PITCH[row, col] = num # assign player coordinates on pitch


field_players("HOME")
field_players("AWAY")


print(GRID)
print(f"rows: {len(PITCH)}")
print(f"columns: {len(PITCH[0])}")
print("\nScan for passing lanes...")

MINUTE = 0
FULL_TIME = 90

HOME_SCORE = 0
AWAY_SCORE = 0

player_position = POSITION_COORDINATES["RM"]["AWAY"]
BALL_POS = player_position

# print(player_position)
total_passes = []
while MINUTE < FULL_TIME:
    MINUTE+=5

    scan = scan_pitch(PITCH, player_position, "AWAY")
    if scan is None:
        # no pass found, take action e.g. dribble
        possess = in_possession(PITCH, BALL_POS)
        print(f"{possess['team']} |\t{possess['name']} - {possess['pos']}")
        team_reposition(PITCH, possess["team"], possess["pos"], BALL_POS)
        display(GRID)
        continue

    check_scan = scan
    player = check_scan["player"] # player coordinates
    BALL_POS = check_scan["path"][-1] # e.g [(1,2), (0,3), (2,1)] (0 idx from player, -1 idx current player)
    possess = in_possession(PITCH, BALL_POS)
    print(f"{possess['team']} |\t{possess['name']} - {possess['pos']}")
    team_reposition(PITCH, possess["team"], possess["pos"], BALL_POS)
    player_position = player
    total_passes.append(MINUTE)
    display(GRID)


print(f"Total Passes {len(total_passes)}")
print("Away Six Yard Box: \n{}".format(AWAY_6_YARD_BOX))
