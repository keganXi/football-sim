from players import HOME_PLAYERS, AWAY_PLAYERS


DEFENCE = ["CB", "RCB", "LCB"] # center halves

ATTACK = ["RS", "LS", "ST"]


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


def push_midfield_up_the_pitch():
    pass


def team_reposition(grid, team, pos, ball_pos):
    """
        NOTE: team awareness is based on where the ball is
        and who'm the ball is with (home/away player)
    """
    if pos in DEFENCE:
      # push attack up the pitch
      push_attack_up_the_pitch(grid)
    pass
