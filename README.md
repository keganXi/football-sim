
# Football Simulator

A brief description of what this project does and who it's for




## Documentation

[Documentation](https://linktodocumentation)

1. Look for players.
- Use DFS (Depth-first search) algorithm to look for players on the pitch (Matrix).

2. Populate pitch.
- Add home/away players (1/-1) to the pitch according to they're position using coordinates e.g. "ST" -> (0, 5)

3. Passing lanes (options), we check if the player is on the same coordinates as from where the pass is coming from (either row/col).
- Horizontal
- Diagonal
- Vertical
- Broken/Curve

4. Check if there are any surrounding players close to the open player and if there is, check how far the ball has to travel vs how close the oppostion player is to the player/ball.
