class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        
        x, y = len(grid), len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
        queue = deque([(0, 0)])
        visited = set()
        
        depth = 0
        while queue:
            depth += 1
            for _ in range(len(queue)):
                cur_x, cur_y = queue.popleft()
                
                if cur_x == x-1 and cur_y == y-1:
                    return depth
                
                if (cur_x, cur_y) not in visited:
                    visited.add((cur_x, cur_y))
                    for dx, dy in directions:
                        new_x = cur_x + dx
                        new_y = cur_y + dy
                        if 0 <= new_x < x and 0 <= new_y < y and grid[new_x][new_y] == 0: 
                            queue.append((new_x, new_y))
        return -1