class Solution:
    def minimumEffortPath(self, heights):
        m, n = len(heights), len(heights[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        def dfs(LIMIT, x, y):
            visited.add((x, y)) 
            for dx, dy in directions:
                if 0 <= dx + x < m and 0 <= dy + y < n and (dx + x, dy + y) not in visited:
                    if abs(heights[x][y] - heights[dx + x][dy + y]) <= LIMIT:
                        dfs(LIMIT, dx + x, dy + y)
        
        beg, end = 0, max(max(heights, key = max))
        while beg < end:
            mid = (beg + end) // 2
            visited = set()
            dfs(mid, 0, 0)
            if (m - 1, n - 1) in visited:
                end = mid
            else:
                beg = mid + 1
                
        return end