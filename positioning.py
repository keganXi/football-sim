from typing import List
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
    for hp in HOME_PLAYERS:
        if hp["coord"] == coord:
            return True
    return False


def press_high(grid, ball_pos):
    print("High Press")
    row, col = ball_pos

    for ap in AWAY_PLAYERS:
        ap_row, ap_col = ap["coord"] # (row, col)

        if ap["role"] in ATTACK:
            press_row = row-3
            new_pos = (press_row, ap_col)
            while is_occupied(new_pos):
                new_pos = (press_row+1, ap_col)
            ap["coord"] = new_pos
            grid[ap_row, ap_col] = 0
            grid[new_pos] = -1

        elif ap["role"] in MIDFIELD:
            press_row = row -6
            new_pos = (press_row, ap_col)
            while is_occupied(new_pos):
                new_pos = (press_row+1, ap_col)
            ap["coord"] = new_pos
            grid[ap_row, ap_col] = 0
            grid[new_pos] = -1

        if ap["role"] in DEFENCE:
            press_row = MIDDLE_THIRD.index.tolist()[len(MIDDLE_THIRD.index.tolist())//2]
            new_pos = (press_row, ap_col)
            while is_occupied(new_pos):
                new_pos = (press_row+1, ap_col)
            ap["coord"] = new_pos
            grid[ap_row, ap_col] = 0
            grid[new_pos] = -1



def team_reposition(grid, team, pos, ball_pos):
    """
        NOTE: team awareness is based on where the ball is
        and who'm the ball is with (home/away player)
    """
    if pos in DEFENCE + ["GK"]:
        press_high(grid, ball_pos) # opposition press

    elif pos in MIDFIELD:
        press_high(grid, ball_pos) # opposition press
