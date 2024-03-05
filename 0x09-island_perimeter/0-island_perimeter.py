#!/usr/bin/python3
""" Module of island perimeter calculation """


def island_perimeter(grid):
    """
    Function that returns the perimeter of the island described in grid
    """
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Start with 4 sides
                perimeter += 4

                # Check for neighboring land cells
                if i > 0 and grid[i - 1][j] == 1:
                    # Reduce 2 sides if neighbor exists in the top
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    # Reduce 2 sides if neighbor exists on the left
                    perimeter -= 2

    return perimeter
