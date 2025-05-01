DEFENCE = ["CB", "RCB", "LCB"] # center halves


def push_attack_up_the_pitch(grid):
    rows = len(grid)
    cols = len(grid[0])



def push_midfield_up_the_pitch():
    pass


def team_awareness(grid, team, pos, ball_pos):
    """
        NOTE: team awareness is based on where the ball is
        and who'm the ball is with (home/away player)
    """
    if pos in DEFENCE:
      # push attack up the pitch
      push_attack_up_the_pitch(grid)
    pass
