from players import HOME_PLAYERS, AWAY_PLAYERS
from passing import POSITION_COORDINATES


def in_possession(grid, coord, team):
    """
        NOTE: find team (HOME/AWAY) that are in possession of the ball
    """
    name = None
    pos = None
    players = HOME_PLAYERS if team == "HOME" else AWAY_PLAYERS

    for player in players:
        row, col = player["coord"]
        if (row, col) == coord:
            name = player["name"]
            pos = player["role"]
            break

    return {
        "team": team,
        "name": name,
        "pos": pos
    }
