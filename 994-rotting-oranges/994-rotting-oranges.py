class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        move_dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        nums_row, nums_col = len(grid), len(grid[0])
        queue = deque()
        cache = []
        time = 0
        
        # visited = set()
        for x in range(nums_row):
            for y in range(nums_col):
                if grid[x][y] == 2:
                    queue.append((x, y))
                    # visited.add((x, y))
        
        while queue or cache:
            
            # time elapsed
            if not queue:
                queue.extend(cache)
                cache.clear()
                time += 1
            
            x, y = queue.popleft()
            for move_dir in move_dirs:
                dx, dy = x + move_dir[0], y + move_dir[1]
                if 0 <= dx < nums_row and 0 <= dy < nums_col and grid[dx][dy] == 1:
                    grid[dx][dy] = 2
                    cache.append((dx, dy))
        
        for x in range(nums_row):
            for y in range(nums_col):
                if grid[x][y] == 1:
                    return -1
                
        return time
            