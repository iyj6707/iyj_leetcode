class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        num_rows, num_cols = len(mat), len(mat[0])

        queue = deque()
        visited = set()
        for x in range(num_rows): 
            for y in range(num_cols): 
                if mat[x][y] == 0:
                    queue.append((x, y))
                    visited.add((x, y))

        count = len(queue)
        step = 1
        move_dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while queue:
            new_count = 0 
            while count > 0:
                x, y = queue.popleft()
                count -= 1                
                for move_dir in move_dirs:
                    dx = x + move_dir[0]
                    dy = y + move_dir[1]
                    if 0 <= dx < num_rows and 0 <= dy < num_cols and mat[dx][dy] != 0 and (dx, dy) not in visited: 
                        new_count += 1
                        visited.add((dx, dy))
                        mat[dx][dy] = step
                        queue.append((dx, dy))
            count = new_count  
            step += 1
        return mat