from passing import get_passing_lane_and_path


def scan_pitch(grid, position, visited=None):
    # NOTE: Depth-first search
    if visited is None:
        visited = set()

    visited.add(position)

    # Check adjacent positions (up, down, left, right)
    row, col = position
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc

        # Ensure the new position is within bounds and not already visited
        if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and (new_row, new_col) not in visited:
            if grid[new_row, new_col] != 0 and grid[new_row, new_col] != -1:  # Check if it's occupied (player present)
                start = next(iter(visited))
                print(start)
                pass_type, path = get_passing_lane_and_path(start, (new_row, new_col))
                print(pass_type)
                return (new_row, new_col)
            else:
                result = scan_pitch(grid, (new_row, new_col), visited)
                if result is not None:
                    return result
