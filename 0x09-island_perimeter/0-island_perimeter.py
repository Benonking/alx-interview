#!/usr/bin/python3
'''
Module Island perimeter
'''


def island_perimeter(grid):
    '''
    Args:
        grid: list of intergers
            0- represents water
            1 rep land
        Approach: Depth first search
    Returns: perimeter of an island described in a grid
    '''
    # get matrix dimensions
    if not grid or not grid[0]:
        return 0
    rows = len(grid)
    cols = len(grid[0])

    def dfs(row, col):
        if row < 0 or row >= rows or col < 0 or \
                col > cols or grid[row][col] == 0:
            return 1
        if grid[row][col] == -1:
            return 0  # already visited

        # set node to already visited
        grid[row][col] = -1
        perimeter = dfs(row-1, col) + dfs(row+1, col) + \
            dfs(row, col - 1) + dfs(row, col + 1)
        return perimeter

    # Find the first land cell to start the traversal
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                return dfs(row, col)
    # No island found
    return 0
