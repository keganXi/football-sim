from players import HOME_PLAYERS, AWAY_PLAYERS
from pitch import (
    AWAY_FINAL_THIRD,
    DEFENSIVE_THIRD,
    HOME_FINAL_THIRD,
    MIDDLE_THIRD,
    HOME_DEFENSIVE_THIRD,
    AWAY_DEFENSIVE_THIRD)


DEFENCE = ["CB", "RCB", "LCB", "RB", "LB"] # center halves

ATTACK = ["RS", "LS", "ST"]

MIDFIELD = ["CM", "LCM", "RCM", "CDM", "LM", "RM", "RDM", "LDM", "CAM"]


def is_occupied(coord):
    for ap in AWAY_PLAYERS:
        if ap["coord"] == coord:
            return True
    return False


def push_attack_up_the_pitch(grid):
    rows = len(grid)
    cols = len(grid[0])
    new_pos = None
    ap_row, ap_col = (0,0)
    for ap in AWAY_PLAYERS:
        if ap["role"] in DEFENCE:
            ap_row, ap_col = ap["coord"]

    for hp in HOME_PLAYERS:
        hp_row, hp_col = hp["coord"] # (row, col) on pitch
        if hp["role"] in ATTACK:
            new_pos = (ap_row, ap_col+1) # new position (next to cb)
            if not is_occupied(new_pos):
                hp["coord"] = new_pos # add new position to player
                grid[new_pos] = 1 # reposition home player


def press_high(grid, ball_pos):
    print("High Press")
    row, col = ball_pos
    third_row = None

    if row >= HOME_DEFENSIVE_THIRD.index.tolist()[0]:
        third_row = HOME_DEFENSIVE_THIRD.index.tolist()[0]

    for ap in AWAY_PLAYERS:
        ap_row, ap_col = ap["coord"] # (row, col)

        if ap["role"] in ATTACK:
            new_pos = (row-2, ap_col)
            ap["coord"] = new_pos
            grid[ap_row, ap_col] = 0
            grid[new_pos] = -1

        elif ap["role"] in MIDFIELD:
            new_pos = (third_row, ap_col)
            ap["coord"] = new_pos
            grid[ap_row, ap_col] = 0
            grid[new_pos] = -1

        elif ap["role"] in DEFENCE:
            def_press = MIDDLE_THIRD.index.tolist()[3]
            new_pos = (def_press, ap_col)
            ap["coord"] = new_pos
            grid[ap_row, ap_col] = 0
            grid[new_pos] = -1




def team_reposition(grid, team, pos, ball_pos):
    """
        NOTE: team awareness is based on where the ball is
        and who'm the ball is with (home/away player)
    """
    if pos in DEFENCE + ["GK"]:
      # push attack up the pitch
      # push_attack_up_the_pitch(grid)
      press_high(grid, ball_pos)
      pass
