def display(grid):
    for col in range(grid.shape[1]):
        print(f"  {col:>3}", end=" ")  # Print column indices
    print()  # New line

    for row in range(grid.shape[0]):
        print(f"{row:>3} ", end="")  # Print row index
        for col in range(grid.shape[1]):
            value = grid.iloc[row, col]
            if value == 1:
                print("\033[94m{:>3}\033[0m", end=" ")  # Blue for Team A
            elif value == -1:
                print("\033[91m{:>3}\033[0m", end=" ")  # Red for Team B
            else:
                print("\033[92m{:>3}\033[0m", end=" ")  # Green for Empty Cell
        print()
