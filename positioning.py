from typing import List
import math
from collections import deque
from players import HOME_PLAYERS, AWAY_PLAYERS
from pitch import (
    AWAY_FINAL_THIRD,
    DEFENSIVE_THIRD,
    GRID,
    HOME_FINAL_THIRD,
    MIDDLE_THIRD,
    HOME_DEFENSIVE_THIRD,
    AWAY_DEFENSIVE_THIRD)


DEFENCE = ["CB", "RCB", "LCB", "RB", "LB"] # center halves

ATTACK = ["RS", "LS", "ST", "LW", "RW"]

MIDFIELD = ["CM", "LCM", "RCM", "CDM", "LM", "RM", "RDM", "LDM", "CAM"]


def is_occupied(coord, players):
    """
        NOTE: check if grid coordinates is not already occupied by player.
    """
    return any(player["coord"] == coord for player in players)



def spatial_awareness(
    coord,
    min_rows=0, min_cols=0,
    max_rows=len(GRID), max_cols=len(GRID[0])) -> tuple | None:
    visited = set()
    queue = deque()
    queue.append(coord)

    while queue:
        current = queue.popleft()

        row, col = current
        if (min_rows <= row < max_rows and min_cols <= col < max_cols and
            current not in visited and not is_occupied(current, AWAY_PLAYERS) and not is_occupied(current, HOME_PLAYERS)):
            return current  # Found open space

        visited.add(current)

        # Add neighboring positions (up, down, left, right)
        neighbors = [
            (row - 1, col),  # up
            (row + 1, col),  # down
            (row, col - 1),  # left
            (row, col + 1),  # right
        ]

        for n in neighbors:
            if n not in visited:
                queue.append(n)

    return None  # No open space found (unlikely unless grid is full)



def get_def_coord():
    coord = []
    for ap in AWAY_PLAYERS:
        if ap["role"] in DEFENCE:
            coord.append((ap["coord"]))

    return coord[0] # return the 1st dataset in the list



def get_att_coord():
    coord = []
    for ap in HOME_PLAYERS:
        if ap["role"] in ATTACK:
            coord.append((ap["coord"]))

    return coord[0] # return the 1st dataset in the list



def push_up_cf(grid, ball_pos):
    row, col = ball_pos

    for hp in HOME_PLAYERS:
        if hp["coord"] != ball_pos and hp["role"] in ["ST", "CF"]:
            hp_row, hp_col = hp["coord"]
            # Idea: player positioning depends on speed e.g. how far he can travel up the pitch.
            def_coord = get_def_coord()
            def_row, _ = def_coord
            new_coord = spatial_awareness(def_coord, min_rows=def_row, min_cols=8, max_cols=12)
            if new_coord is not None:
                new_row, new_col = new_coord
                grid[hp_row, hp_col] = 0 # remove player previous position (grid)
                hp["coord"] = new_coord # add new position to player coord
                grid[new_row, new_col] = 1 # player new grid position



def push_up_cam(grid, ball_pos):
    row, col = ball_pos

    for hp in HOME_PLAYERS:
        if hp["coord"] != ball_pos and hp["role"] in ["CAM"]:
            hp_row, hp_col = hp["coord"]
            # Idea: CAM has to position themeself to be in a position to receive the ball
            # depending on ball coordinates (depending on positioning rating)
            att_coord = get_att_coord()
            att_row, att_col = att_coord
            new_coord = spatial_awareness(att_coord, min_rows=att_row+2, min_cols=8, max_cols=12)
            if new_coord is not None:
                new_row, new_col = new_coord
                grid[hp_row, hp_col] = 0
                hp["coord"] = new_coord
                grid[new_row, new_col] = 1



def push_up_cb(grid, ball_pos):
    row, col = ball_pos
    for hp in HOME_PLAYERS:
        if hp["coord"] != ball_pos and hp["role"] in ["CB", "LCB", "RCB"]:
            hp_row, hp_col = hp["coord"]
            row = MIDDLE_THIRD.index[-1]
            new_coord = spatial_awareness((row, hp_col), min_rows=row, min_cols=6, max_cols=14)
            if new_coord is not None:
                new_row, new_col = new_coord
                grid[hp_row, hp_col] = 0 # remove player previous position (grid)
                hp["coord"] = (new_row, new_col) # add new position to player coord
                grid[new_row, new_col] = 1 # player new grid position



def push_up_cm(grid, ball_pos):
    row, col = ball_pos
    for hp in HOME_PLAYERS:
        if hp["coord"] != ball_pos and hp["role"] in ["CM", "RCM", "LCM"]:
            hp_row, hp_col = hp["coord"]
            row = MIDDLE_THIRD.index[3]
            new_coord = spatial_awareness((row, hp_col), min_rows=row, min_cols=6, max_cols=14)
            if new_coord is not None:
                new_row, new_col = new_coord
                grid[hp_row, hp_col] = 0 # remove player previous position (grid)
                hp["coord"] = (new_row, new_col) # add new position to player coord
                grid[new_row, new_col] = 1 # player new grid position



def push_up_wide_players(grid, ball_pos, role):
    MAX_COLS = 0
    MIN_COLS = 0
    if role in ["LM", "LB"]:
        MAX_COLS = 3
        MIN_COLS = 0
    elif role in ["RM", "RB"]:
        MAX_COLS = 21
        MIN_COLS = 17

    for hp in HOME_PLAYERS:
        if hp["coord"] != ball_pos and hp["role"] in [role]:
            hp_row, hp_col = hp["coord"]
            row, _ = get_def_coord()
            if hp["role"] in ["LB", "RB"]:
                row = MIDDLE_THIRD.index[4]
            new_coord = spatial_awareness((row, hp_col), min_rows=row, max_cols=MAX_COLS, min_cols=MIN_COLS)
            if new_coord is not None:
                new_row, new_col = new_coord
                grid[hp_row, hp_col] = 0 # remove player previous position (grid)
                hp["coord"] = new_coord # add new position to player coord
                grid[new_row, new_col] = 1 # player new grid position



def low_block(grid):
    for ap in AWAY_PLAYERS:
        ap_row, ap_col = ap["coord"]
        if ap["role"] in ["CB", "LCB", "RCB", "RB", "LB"]:
            row = AWAY_DEFENSIVE_THIRD.index[3]
            # can tighten low block (CB narrow space)
            grid[ap_row, ap_col] = 0
            ap["coord"] = (row, ap_col)
            grid[row, ap_col] = -1

        elif ap["role"] in ["CDM", "RDM", "LDM", "RCM", "LCM"]:
            row = row = AWAY_DEFENSIVE_THIRD.index[5]
            grid[ap_row, ap_col] = 0
            ap["coord"] = (row, ap_col)
            grid[row, ap_col] = -1

        elif ap["role"] in ["RM", "LM", "RW", "LW"]:
            row = row = AWAY_DEFENSIVE_THIRD.index[5]
            grid[ap_row, ap_col] = 0
            ap["coord"] = (row, ap_col)
            grid[row, ap_col] = -1

        elif ap["role"] in ["ST", "CF"]:
            row = row = MIDDLE_THIRD.index[2]
            grid[ap_row, ap_col] = 0
            ap["coord"] = (row, ap_col)
            grid[row, ap_col] = -1



def closest_pressure(grid, ball_pos):
    """
        NOTE: find the closest player to the ball coordinates, and
        reposition player coordinates in a pressure position.
    """
    closest = (0, 0)
    min_dist = float('inf')

    for ap in AWAY_PLAYERS:
        op_coord = ap["coord"]
        dist = math.sqrt((ball_pos[0] - op_coord[0])**2 + (ball_pos[1] - op_coord[1])**2)

        if dist < min_dist:
            min_dist = dist
            closest = op_coord

    row, col = closest
    for ap in AWAY_PLAYERS:
        if ap["coord"] == (row, col):
            new_coord = spatial_awareness(ball_pos)
            if new_coord is not None:
                ap_row, ap_col = new_coord
                grid[row, col] = 0
                ap["coord"] = new_coord
                grid[ap_row, ap_col] = -1
                break


def team_reposition(grid, team, pos, ball_pos):
    """
        NOTE: team awareness is based on where the ball is
        and who'm the ball is with (home/away player)
    """
    # low_block(grid)
    push_up_cf(grid, ball_pos) # Centre Forward
    push_up_cam(grid, ball_pos) # Attacking Midfield
    push_up_cm(grid, ball_pos) # Centre Midfield
    push_up_wide_players(grid, ball_pos, "LM")
    push_up_wide_players(grid, ball_pos, "RM")
    push_up_wide_players(grid, ball_pos, "LB")
    push_up_wide_players(grid, ball_pos, "RB")
    push_up_cb(grid, ball_pos) # Centre Backs
    closest_pressure(grid, ball_pos)
