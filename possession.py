from players import HOME_PLAYERS, AWAY_PLAYERS
from passing import POSITION_COORDINATES


def in_possession(grid, coord):
    """
        NOTE: find team (HOME/AWAY) that are in possession of the ball
    """
    team = None
    name = None
    pos = None
    for key, value in POSITION_COORDINATES.items():
        if value["HOME"] == coord:
            team = "HOME"
            pos = key
        elif value["AWAY"] == coord:
            team = "AWAY"
            pos = key

        if team is not None and key == pos:
            players = AWAY_PLAYERS if team == "AWAY" else HOME_PLAYERS
            for item in players:
                if pos == item["role"]:
                    name = item["name"]
    return {
        "team": team,
        "name": name,
        "pos": pos
    }
