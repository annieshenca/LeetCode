class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])
        count = 0
        
        # Loop through the x and y of the grid.
        # Each time we encounter a '1', increment count by 4.
        # Then check if there is also a '1' to the right or below,
        # if so, decrement by 2 for each '1'.
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    count += 4
                    if r < row-1 and grid[r+1][c] == 1:
                        count -= 2
                    if c < col-1 and grid[r][c+1] == 1:
                        count -= 2
        
        return count
