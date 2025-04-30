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



# (0, 0) -> (row, col)
POSITION_COORDINATES = {
    "GK": {
        "HOME": (23, 9),
        "AWAY": (0, 9),
    },

    # Defence
    "CB": {
        "HOME": (19, 9),
        "AWAY": (4, 9),
    },
    "LCB": {
        "HOME": (20, 6),
        "AWAY": (3, 12),
    },
    "RCB": {
        "HOME": (20, 12),
        "AWAY": (3, 6),
    },
    "LB": {
        "HOME": (19, 0),
        "AWAY": (4, 18),
    },
    "RB": {
        "HOME": (19, 18),
        "AWAY": (4, 0),
    },

    # Midfield
    "LCM": {
        "HOME": (18, 6),
        "AWAY": (5, 12),
    },
    "RCM": {
        "HOME": (18, 12),
        "AWAY": (5, 6),
    },
    "RM": {
        "HOME": (15, 18),
        "AWAY": (8, 0),
    },
    "CAM": {
        "HOME": (16, 9),
        "AWAY": (7, 9),
    },
    "LM": {
        "HOME": (15, 0),
        "AWAY": (8, 18),
    },

    # Attack
    "ST": {
        "HOME": (13, 9),
        "AWAY": (10, 9),
    },
}
