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


def is_occupied(coord, players):
    for hp in players:
        if hp["coord"] == coord:
            return True
    return False


def press_high(grid, ball_pos):
    print("High Press")
    row, col = ball_pos
    third: List = MIDDLE_THIRD.index.tolist()
    if row <= HOME_DEFENSIVE_THIRD.index.tolist()[0]:
        third = AWAY_DEFENSIVE_THIRD.index.tolist()

    for ap in AWAY_PLAYERS:
        ap_row, ap_col = ap["coord"] # (row, col)

        if ap["role"] in ATTACK:
            press_row = row-3
            new_pos = (press_row, ap_col)
            while is_occupied(new_pos, HOME_PLAYERS):
                new_pos = (press_row+1, ap_col)
            ap["coord"] = new_pos
            grid[ap_row, ap_col] = 0
            grid[new_pos] = -1

        elif ap["role"] in MIDFIELD:
            press_row = row -6
            new_pos = (press_row, ap_col)
            while is_occupied(new_pos, HOME_PLAYERS):
                new_pos = (press_row+1, ap_col)
            ap["coord"] = new_pos
            grid[ap_row, ap_col] = 0
            grid[new_pos] = -1

        if ap["role"] in DEFENCE:
            press_row = third[len(third)//2]
            new_pos = (press_row, ap_col)
            while is_occupied(new_pos, HOME_PLAYERS):
                new_pos = (press_row+1, ap_col)
            ap["coord"] = new_pos
            grid[ap_row, ap_col] = 0
            grid[new_pos] = -1



def forward_run(grid, ball_pos, positions):
    print("Forward Run")
    row, col = ball_pos
    final_third = HOME_FINAL_THIRD.index.tolist()

    for hp in HOME_PLAYERS:
        hp_row, hp_col = hp["coord"]
        if (hp_row, hp_col) == ball_pos:
            continue

        if hp["role"] in positions:
            # Calculate target position in final third
            target_row = final_third[len(final_third)//2]

            # Try to find space away from opposition players first
            space_found = False
            for r in range(final_third[0], final_third[-1]):
                for c in range(hp_col-3, hp_col+3):
                    if (r,c) not in [p["coord"] for p in AWAY_PLAYERS]:
                        # Check if position can receive pass from ball_pos
                        if abs(r - row) <= 1 and abs(c - col) <= 1:
                            new_pos = (r,c)
                            print(f"found path")
                            if not is_occupied(new_pos, AWAY_PLAYERS):
                                hp["coord"] = new_pos
                                grid[hp_row, hp_col] = 0
                                grid[new_pos] = 1
                                space_found = True

            # If no space found, position 2 cells away from defence
            if not space_found:
                for ap in AWAY_PLAYERS:
                    if ap["role"] in DEFENCE:
                        def_row, def_col = ap["coord"]
                        new_pos = (def_row + 1, hp_col)
                        if ap["coord"] != new_pos:
                            hp["coord"] = new_pos
                            grid[new_pos] = 1
                            grid[hp_row, hp_col] = 0
                            print(f"{hp['name']}")
                            break


def team_reposition(grid, team, pos, ball_pos):
    """
        NOTE: team awareness is based on where the ball is
        and who'm the ball is with (home/away player)
    """
    if pos in DEFENCE + ["GK"]:
        press_high(grid, ball_pos) # opposition press

    elif pos in MIDFIELD:
        forward_run(grid, ball_pos, ATTACK+["LM", "RM"])
        press_high(grid, ball_pos) # opposition press

    elif pos in ATTACK:
        pass
