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
            team = "HOME"
            name = player["name"]
            pos = player["role"]
        elif player["coord"] == coord:
            team = "AWAY"
            name = ["name"]
            pos = ["role"]

    return {
        "team": team,
        "name": name,
        "pos": pos
    }
