# Grid (Pitch)
#
#   0   1   2   3   4   5   6   7   8 (-1)
#   A   B   C   D   E   F   G   H   I
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9 (-1)


# (0, 0) -> (row, col)
POSITION_COORDINATES = {
    "GK": {
        "HOME": (-1, 4),
        "AWAY": (0, 4),
    },
    "DF": {
        "HOME": (7, 4),
        "AWAY": (2, 4),
    },
    "RM": {
        "HOME": (5, -1),
        "AWAY": (5, 1),
    },
    "LM": {
        "HOME": (5, 0),
        "AWAY": (5, -2),
    },
    "ST": {
        "HOME": (1, 4),
        "AWAY": (8, 4),
    },
}
