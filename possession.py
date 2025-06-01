from players import HOME_PLAYERS, AWAY_PLAYERS
from passing import POSITION_COORDINATES


def in_possession(grid, coord):
    """
        NOTE: find team (HOME/AWAY) that are in possession of the ball
    """
    team = None
    name = None
    pos = None
    data = [*HOME_PLAYERS, *AWAY_PLAYERS]

    for player in data:

        if player["coord"] == coord:
            name = player["name"]
            pos = player["role"]
            break

    return {
        "team": "AWAY",
        "name": name,
        "pos": pos
    }
