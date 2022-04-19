class Solution:
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = 0
        x, y = len(grid), len(grid[0])
        
        def dfs(m, n) -> int:
            if not ((0 <= m < x) and (0 <= n < y)):
                return 0
            
            if grid[m][n] == 0:
                return 0
            
            grid[m][n] = 0
            
            return 1 + dfs(m+1, n) + dfs(m, n+1) + dfs(m-1, n) + dfs(m, n-1)
           
        for m in range(x):
            for n in range(y):
                if grid[m][n] == 1:
                    area = max(area, dfs(m, n))
        return area
                    
        
            