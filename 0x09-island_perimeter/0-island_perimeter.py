#!/usr/bin/python3
"""Island perimeter computing module.
"""


def island_perimeter(grid):
    '''
    Args:
         grid: list of intergers
             0- represents water
             1 rep land
         Approach: Depth first search
    Returns: perimeter of an island described in a grid
    linear solutuion'''
    perimeter = 0
    if type(grid) != list:
        return 0
    n = len(grid)
    for i, row in enumerate(grid):
        m = len(row)
        for j, cell in enumerate(row):
            if cell == 0:
                continue
            edges = (
                i == 0 or (len(grid[i - 1]) > j and grid[i - 1][j] == 0),
                j == m - 1 or (m > j + 1 and row[j + 1] == 0),
                i == n - 1 or (len(grid[i + 1]) > j and grid[i + 1][j] == 0),
                j == 0 or row[j - 1] == 0,
            )
            perimeter += sum(edges)
    return perimeter
# #!/usr/bin/python3
# '''
# Module Island perimeter
# '''


# def island_perimeter(grid):
#     '''
#     Args:
#         grid: list of intergers
#             0- represents water
#             1 rep land
#         Approach: Depth first search
#     Returns: perimeter of an island described in a grid
#     Recursive solutuion
#     '''
#     # get matrix dimensions
#     if not grid or not grid[0]:
#         return 0
#     rows = len(grid)
#     cols = len(grid[0])

#     def dfs(row, col):
#         if row < 0 or row >= rows or col < 0 or \
#                 col > cols or grid[row][col] == 0:
#             return 1
#         if grid[row][col] == -1:
#             return 0  # already visited

#         # set node to already visited
#         grid[row][col] = -1
#         perimeter = dfs(row-1, col) + dfs(row+1, col) + \
#             dfs(row, col - 1) + dfs(row, col + 1)
#         return perimeter

#     # Find the first land cell to start the traversal
#     for row in range(rows):
#         for col in range(cols):
#             if grid[row][col] == 1:
#                 return dfs(row, col)
#     # No island found
#     return 0
