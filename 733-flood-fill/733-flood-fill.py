class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        startColor = image[sr][sc]
        image[sr][sc] = newColor
        tiles = deque([(sr, sc)])
        m, n = len(image[0]), len(image)
        
        while tiles:
            a, b = tiles.popleft()
            print(a, b)
            
            if a - 1 >= 0 and image[a-1][b] == startColor and image[a-1][b] != newColor:
                image[a-1][b] = newColor
                tiles.append((a-1, b))
            if b - 1 >= 0 and image[a][b-1] == startColor and image[a][b-1] != newColor:
                image[a][b-1] = newColor
                tiles.append((a, b-1))
            if a + 1 < n and image[a+1][b] == startColor and image[a+1][b] != newColor:
                image[a+1][b] = newColor
                tiles.append((a+1, b))
            if b + 1 < m and image[a][b+1] == startColor and image[a][b+1] != newColor:
                image[a][b+1] = newColor
                tiles.append((a, b+1))
        
        return image