"""
Algo: Iterate through each of the cell and if it is an island, do dfs to mark all           adjacent islands, then increase the counter by 1

T.C. - O(M*N) - 'M' rows and 'N' columns
"""

class Solution:
    def numIslands(self, grid):
        
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        if not grid: # If there is no grid
            return 0
        
        count = 0 # Count of number of islands
        
        for i in range(len(grid)):
            for j in range(len(grid[0])): # Iterating over each value in each row
                if (grid[i][j] == '1'):
                    
                    self.dfs(grid, i, j)
                    count += 1
                    
        return count
    
    
    # dfs function making connected 1's replacing by '#' recursively in it
    def dfs(self, grid, i, j):
        if (i<0 or j<0 or i>= len(grid) or j>= len(grid[0]) or grid[i][j] != '1'):
            return
        
        grid[i][j] = '#'
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)
        
        
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
        ]

print(Solution().numIslands(grid))