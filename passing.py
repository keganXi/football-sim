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

from pitch import PITCH, PITCH_LANE, DEFENSIVE_THIRD, MIDDLE_THIRD, FINAL_THIRD


def get_passing_lane_and_path(start, end):
    x1, y1 = start
    x2, y2 = end
    path = []

    if x1 == x2:
        # horizontal pass (row stays same, move across columns)
        step = 1 if y2 > y1 else -1
        for y in range(y1, y2 + step, step):
            path.append((x1, y))
        pass_type = "horizontal pass"

    elif y1 == y2:
        # vertical pass (column stays same, move across rows)
        step = 1 if x2 > x1 else -1
        for x in range(x1, x2 + step, step):
            path.append((x, y1))
        pass_type = "vertical pass"

    elif abs(x2 - x1) == abs(y2 - y1):
        # diagonal pass
        step_x = 1 if x2 > x1 else -1
        step_y = 1 if y2 > y1 else -1
        x, y = x1, y1
        while (x, y) != (x2 + step_x, y2 + step_y):
            path.append((x, y))
            x += step_x
            y += step_y
        pass_type = "diagonal pass"

    else:
        # Complex pass (needs smarter path finding like A* maybe)
        pass_type = "complex pass (not straight or diagonal)"
        path = None

    return pass_type, path


CENTER = int(len(PITCH[0])/2) # center col
LAST = int(len(PITCH)-1) # last row
RIGHT = int(len(PITCH[0])-1)




# (0, 0) -> (row, col)
POSITION_COORDINATES = {
    "GK": {
        "HOME": (LAST, CENTER),
        "AWAY": (0, CENTER),
    },

    # Defence
    "CB": {
        "HOME": (LAST-4, CENTER),
        "AWAY": (4, CENTER),
    },
    "LCB": {
        "HOME": (LAST-4, CENTER-2),
        "AWAY": (4, CENTER+2),
    },
    "RCB": {
        "HOME": (LAST-4, CENTER+2),
        "AWAY": (4, CENTER-2),
    },
    "LB": {
        "HOME": (LAST-6, 0),
        "AWAY": (6, RIGHT),
    },
    "RB": {
        "HOME": (LAST-6, RIGHT),
        "AWAY": (6, 0),
    },

    # Midfield
    "LCM": {
        "HOME": (LAST-8, CENTER-2),
        "AWAY": (8, CENTER+2),
    },
    "RCM": {
        "HOME": (LAST-8, CENTER+2),
        "AWAY": (8, CENTER-2),
    },
    "RM": {
        "HOME": (LAST-10, RIGHT),
        "AWAY": (10, 0),
    },
    "CAM": {
        "HOME": (LAST-10, CENTER),
        "AWAY": (10, CENTER),
    },
    "LM": {
        "HOME": (LAST-10, 0),
        "AWAY": (10, RIGHT),
    },

    # Attack
    "ST": {
        "HOME": (LAST-12, CENTER),
        "AWAY": (12, CENTER),
    },
}
