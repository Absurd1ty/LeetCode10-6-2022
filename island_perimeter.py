"""
You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally).
The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't

connected to the water around the island. One cell is a
square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.
"""
class Solution:
    def islandPerimeter(self, grid) -> int:
        perimeter = 0
        row = len(grid)
        col = len(grid[0])

        for i in range(row):
            for j in range(col):

                if grid[i][j] == 1:
                    if i == 0 or grid[i-1][j] != 1:
                        perimeter += 1
                    if j == 0 or grid[i][j-1] != 1:
                        perimeter += 1
                    if j == col-1 or grid[i][j+1] != 1:
                        perimeter += 1
                    if i == row-1 or grid[i+1][j] != 1:
                        perimeter += 1

        return perimeter
test=Solution.islandPerimeter(Solution, [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]])
print(test)