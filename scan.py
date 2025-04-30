from passing import get_passing_lane_and_path


def scan_pitch(grid, position, start=None):
    # NOTE: Depth-first search
    start = position

    # Initialize a stack for DFS and a visited set
    stack = [start]
    visited = set()
    visited.add(start)

    while stack:
        # Get the current position from the stack
        row, col = stack.pop()

        # Check adjacent positions (up, down, left, right)
        directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]  # Up, Down, Left, Right
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc

            # Ensure the new position is within bounds and not already visited
            if (0 <= new_row < len(grid) and
                0 <= new_col < len(grid[0]) and
                (new_row, new_col) not in visited):

                visited.add((new_row, new_col))

                if grid[new_row, new_col] != 0 and grid[new_row, new_col] != -1:  # Check if it's occupied (player present)
                    pass_type, path = get_passing_lane_and_path(start, (new_row, new_col))
                    if path is not None: # passing lane found
                        # print(f"{start} -> {(new_row, new_col)} ({pass_type})")
                        print(f"{start} - {(new_row, new_col)}")
                        return (new_row, new_col)
                else:
                    # Add the new position to the stack for further exploration
                    stack.append((new_row, new_col))

    # No match found after exploring all reachable positions
    return None
